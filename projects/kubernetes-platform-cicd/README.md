# Kubernetes Platform + CI/CD Starter — Generic

## What it is
A minimal, readable platform starter that a DevOps / platform engineer would recognise immediately:

- Terraform (`terraform/`) — generic cloud networking + Kubernetes cluster inputs, with variables instead of hard-coded accounts or regions.
- GitHub Actions (` .github/workflows/ci-cd.yaml` in this folder as `ci-cd.yaml`) — build, test, and deploy on push to main, with a manual approval feel via environment protection in a real repo.
- Kubernetes manifests (`k8s/`) — Deployment with health probes, resource requests/limits, and a rolling update strategy, plus a Service.

## Principles shown
- Infrastructure as code, not click-ops
- Health checks and limits on every workload
- Rollouts that do not take the whole app down at once
- Secrets referenced, never committed (use your own secret manager / GitHub Secrets)

## Run / adapt
Replace the placeholder image, region, and cluster name in Terraform variables and in the workflow. This starter contains no real cloud account, cluster, or credential.
