# vLLM on OpenShift — Lab

## Goal
Run LLM inference on OpenShift in a way a platform team can repeat: one vLLM instance, its own namespace, pointed at a model location, with sane resource requests.

## Lab steps (generic)
1. Install the vLLM operator from the OperatorHub catalog.
2. Create a dedicated namespace for the vLLM instance (single instance in this lab).
3. Point the instance at your model location (storage / model path — replace the placeholder in the manifest).
4. Start small, then tune.

## Tuning notes from real lab experience
- Model length matters: values that are too low break generation in confusing ways. Tune it deliberately, and record what you changed.
- GPU sizing is an open question, not an assumption: test with your actual model and load before promising capacity. In my lab work, whether 2 GPUs per node would be enough was an explicit open question, not a conclusion.
- Keep the LLM side and the OpenShift side separate in your notes: parameter tuning first, operator install and wiring second.

## Manifest
`manifests/vllm-deployment.yaml` is a generic starting point with placeholders for model path, GPU count, and resource limits. It is not a production manifest and contains no real model, cluster, or internal data.

## Why this helps for platform roles
It shows the exact skill platform teams need for AI workloads: operators, namespaces, resource planning, and honest capacity work — not just "we ran a model once."
