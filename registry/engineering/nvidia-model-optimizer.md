---
name: NVIDIA Model Optimizer (ModelOpt)
category: engineering
subcategory: llm-optimization
status: experimental
tier: C
human_reviewed: false
type: framework
canonical_repo: https://github.com/NVIDIA/Model-Optimizer
website: https://nvidia.github.io/Model-Optimizer/
pinned_version: nvidia-modelopt 0.47.0 (PyPI; git tag 0.47.0 → commit c10fb3bf061229798b9e5fc53e5d9dd09c1bc7a5, 2026-09-23)
license: Apache-2.0
score: null
confidence: medium
tested: true
last_verified: 2026-10-19
---

# NVIDIA Model Optimizer — compress and accelerate an existing model

## What it does
A Python library (`nvidia-modelopt`) that takes an existing Hugging Face,
PyTorch, or ONNX model and makes it smaller and faster to serve. It supports
post-training quantization (FP8, INT8, INT4/AWQ, NVFP4) and quantization-aware
training, pruning and NAS, knowledge distillation, speculative decoding
(EAGLE/Medusa draft heads), and sparsity. It exports checkpoints for
TensorRT-LLM, TensorRT, vLLM, and SGLang, and integrates with Megatron-Bridge,
Megatron-LM, and Hugging Face Accelerate.

**It does not create a foundation model.** It optimizes a model you already
have the right to use. "Build your own LLM" with this tool means: start
from an open-weight model, optionally fine-tune it, then compress it for
cheaper inference.

## When to use
- Cutting GPU memory and serving cost of a self-hosted open-weight model
  (quantize to FP8/INT4/NVFP4 and serve with TensorRT-LLM or vLLM)
- Distilling a smaller student from a larger open-weight teacher you are
  licensed to use
- Adding speculative-decoding draft heads to reduce generation latency
- After fine-tuning (LoRA/QLoRA/full), as the compression step before deployment

## When not to use / restrictions
- **Not for training an LLM from scratch** — that needs a pretraining stack and
  large-scale compute; ModelOpt is a post-training/compression layer.
- **Not for hosted-API products.** If the product calls a closed model API, there is
  nothing to optimize locally.
- **Model license still governs.** ModelOpt is Apache-2.0, but the input
  model's license (Llama, Gemma, Qwen, etc.) and any use restrictions carry
  through to the optimized checkpoint.
- **Do not distill from closed-model outputs** (GPT, Claude, Gemini, …) when the
  provider's terms prohibit training competing models on outputs.
- **Untrusted checkpoints are a code-execution risk.** Upstream SECURITY.md
  warns against `pickle`/`torch.load()` on untrusted weights. Load only
  `safetensors` from verified sources; keep `trust_remote_code=False` (the
  default in ModelOpt's loaders) unless the remote code has been reviewed.
- **Accuracy must be re-measured.** Quantization and pruning change outputs;
  always compare against the unoptimized baseline on task-specific evals
  before shipping.
- **Hardware.** Production use needs NVIDIA GPUs; FP8 needs Ada/Hopper or
  newer and NVFP4 needs Blackwell. Custom CUDA kernels are JIT-compiled on
  first use via `torch.utils.cpp_extension`.

## Bundled agent plugin (separate intake)
The repository ships `plugins/modelopt/` — a Claude Code / Codex plugin with
18 skills (PTQ, QAD, deployment, evaluation, EAGLE3 workflows, MLflow,
release tooling) and an MCP server.

- **Not adopted by this record.** The MCP server is registered as
  `uvx --from git+https://github.com/NVIDIA/Model-Optimizer.git#subdirectory=tools/mcp`
  with **no ref**. It runs whatever is on upstream `main` at launch. That is unpinned
  remote code, a prohibited default under
  `governance/AGENT-SKILL-SUPPLY-CHAIN.md`. Pin a reviewed commit
  (`...Model-Optimizer.git@<sha>#subdirectory=tools/mcp`) before any use.
- Several skills are NVIDIA-internal developer workflows (release
  cherry-picks, day-0 release gates, Slurm clusters, MLflow). `common/remote_exec.sh`
  runs commands on remote hosts over multiplexed SSH, and evaluation skills
  read `HF_TOKEN` and cloud keys from the environment. Treat these as
  credential- and remote-execution-bearing; approval required per use.
- SkillSpector per-skill results: see Validation results.

## Evidence
- License Apache-2.0 `[V]` — LICENSE at tag 0.47.0
- Tag `0.47.0` → `c10fb3b…` (lightweight tag, commit dated 2026-09-23) `[V]` —
  `git ls-remote` on 2026-10-19
- PyPI `nvidia-modelopt` 0.47.0 is the latest stable; 0.48.0rc1 exists as a
  pre-release `[V]` — `pip index versions`, `git ls-remote` on 2026-10-19
- Python `>=3.10,<3.15`; core deps include `torch>=2.8`, `safetensors`,
  `pydantic`, `PyYAML`, `omegaconf`, `pulp<4.0` `[V]` — pyproject.toml
- Security guidance on untrusted artifacts and deserialization `[V]` —
  SECURITY.md at tag 0.47.0
- No telemetry/analytics SDK found in `modelopt/` source `[M]` — grep only;
  not verified at runtime
- GPU throughput, accuracy retention on real LLMs, and TensorRT-LLM/vLLM
  export `[U]` — not executed (no GPU in the evaluation environment)

## Validation results (CPU-only sandbox, 2026-10-19)
- Installed `nvidia-modelopt[hf]==0.47.0` from PyPI into an isolated
  Python 3.12 venv with `uv` (pulled `torch 2.14.1+cu130`; ~5.5 GB). No
  upstream install scripts or plugin/MCP components were run.
- **Packaging gap:** bare `nvidia-modelopt` (no extras) fails on
  `import modelopt.torch` with `ModuleNotFoundError: requests`, then
  `huggingface_hub`. Upstream documents `nvidia-modelopt[all]`; use
  `[hf]` at minimum for PyTorch/Hugging Face workflows.
- Smoke test on a toy 2-layer MLP (64→128→16), 8 random calibration batches,
  `HF_HUB_OFFLINE=1`, script run with `python -I`:

  | Config | Result | Relative output error vs FP32 |
  |---|---|---|
  | `INT8_DEFAULT_CFG` | ok, 6 quantizers inserted | 0.0147 |
  | `FP8_DEFAULT_CFG` | ok (simulated/fake-quant on CPU) | 0.0528 |
  | `INT4_AWQ_CFG` | ok (AWQ-lite search ran) | 0.1061 |

  `mto.save` → `mto.restore` round trip reproduced identical outputs.
- This proves the API works end to end on the pinned release. It does **not**
  prove speedups, memory savings, or accuracy on a real LLM, which require GPU
  runs with a task-specific baseline.

## Installation (only after explicit authorization)
`pip install "nvidia-modelopt[hf]==0.47.0"` (or `[all]` for ONNX and
Puzzletron) in an isolated environment on the target GPU host. Pin
`torch`/CUDA to the versions validated for the deployment runtime
(TensorRT-LLM/vLLM). Do not install the bundled plugin or MCP server
without a separate pinned-commit review.

## Agent integration
Typical post-training quantization flow:
`mtq.quantize(model, mtq.FP8_DEFAULT_CFG, forward_loop=calibrate)` → evaluate
against baseline → `export_hf_checkpoint(...)` / TensorRT-LLM export →
serve. Agents may draft configs and scripts; running on GPUs, downloading
gated models (HF token), and deploying are state-changing actions that
need approval.

## Required human review
Input model license and acceptable-use terms; provenance and format of
every checkpoint loaded; accuracy regression vs. baseline before deployment;
any use of the bundled plugin, MCP server, or remote-execution skills; GPU
spend.

## Score notes
Not scored. Provenance is strong (NVIDIA org, tagged releases, PyPI, PSIRT
disclosure path) and the license is clean. The API was functionally verified on CPU only. GPU
performance, real-model accuracy retention, and matched-baseline benefit are
unmeasured, so it remains experimental / tier C.
