# Avinash Nandhyala — Senior Platform / DevOps / SRE Portfolio

GitHub: avinash-nandhyala · LinkedIn: linkedin.com/in/avinash-reddy-203422439 · Email: avinashnandhyala12@gmail.com

No personal location is listed in this portfolio, by design.

This is a **strong, senior-level portfolio** — not a basics collection. It is built for DevOps, Site Reliability, Developer Productivity / Platform, and AI Infrastructure roles at Apple, Google, Amazon, Netflix, Red Hat, ServiceNow, Salesforce, Dynatrace, Cisco, NVIDIA, Samsung and others.

## What I do, in one paragraph

I build platforms that let product teams ship without waiting on tickets, and I make production work observable and automated: multi-cluster Kubernetes with GitOps, zero-trust service mesh, SLO-driven alerting, progressive delivery, and agentic tooling that investigates incidents end to end. The code here proves it — it is runnable, not just described.

## How to read it

- Start with `index.html` — the portfolio site. Open it in any browser, no build step needed.
- Each project in `projects/` is standalone and runnable. Advanced projects are marked ★ on the site.
- Sample data is clearly labelled as sample. No company-confidential code, cluster names, app names, internal tickets, or internal data are included. Projects built for this portfolio are presented as portfolio builds / labs, not as claims about a specific employer's production systems.

## Experience

- **Senior Cloud Engineer — OpenShift** — Oct 2025 to present
- **System Engineer — DevOps, Virtusa** — Jun 2022 to Jul 2023
- **DevOps / Site Reliability Engineer, LTIMindtree** — May 2019 to May 2022

Education: MS in Computer / Information Technology (2023–2025).

Certifications: Certified Kubernetes Administrator (CKA), AWS Certified Solutions Architect, AWS / Azure Certified DevOps Engineer, Linux Foundation Certified System Administrator.

## Senior stack

OpenShift · Kubernetes · Multi-cluster GitOps (ArgoCD) · Service Mesh, mTLS and Zero Trust · AWS · GCP / GKE · Terraform · Ansible · Pulumi · CloudFormation · Python · Go · Bash · Java / Spring Boot · Gradle / Maven · CI/CD and Progressive Delivery · Prometheus, Grafana, Dynatrace, Kiali, OpenTelemetry · SLOs, error budgets, burn-rate alerting · Incident response and blameless postmortems · Generative AI integration and agentic DevOps · vLLM on Kubernetes · Security scanning and policy · Cost optimisation

## Projects — 10, advanced first

1. **multi-cluster-gitops-platform** ★ — One repo, many clusters, no drift. ArgoCD ApplicationSets, environment promotion with gates, policy checks, and a drift report.
2. **agentic-devops-responder** ★ — An LLM incident agent with tools, not just a chatbot: it gathers pod, mesh, and metric evidence, ranks likely causes, and gives a fix I validate and execute end to end.
3. **slo-observability-automation** ★ — SLO definitions, burn-rate alert rules, error-budget math, and runbook linking. Alerts that mean something, with tests for the math.
4. **kubernetes-disaster-recovery-failover** ★ — Multi-region disaster recovery I run end to end: Velero backups, restore drills, RTO/RPO tiers, a failover decision engine, and runbooks for drill, failover, and rollback.
5. **openshift-service-mesh-troubleshooting** — Intake-first mesh diagnostics: routes, gateway hosts, certificates, endpoints, pods. Catches the migration miss where gateway hosts/certs are not updated with routes, causing 503s and SSL errors while pods look healthy.
6. **cluster-audit-decommission** — Audit workloads on a retiring cluster and surface resource-heavy pods, as a shareable list for owners.
7. **team-request-tracker** — Shared-mailbox work made countable and reportable: intake, owner, status, weekly summary.
8. **vllm-on-openshift-lab** — LLM inference on OpenShift with the vLLM operator, model wiring, autoscaling notes, and honest GPU sizing.
9. **kubernetes-platform-cicd** — Terraform, GitHub Actions, canary-ready Kubernetes manifests with probes, limits, and security scanning.
10. **incident-memory** — Searchable incident memory CLI: ask about a symptom, get the previous fix.

## Running the site locally

```bash
cd portfolio
python3 -m http.server 8000
# open http://localhost:8000
```

## Running the advanced projects

See each project's README. In short:

```bash
python3 projects/team-request-tracker/tracker.py --report
python3 projects/incident-memory/incident-memory.py "503 gateway"
python3 projects/slo-observability-automation/slo.py --test
python3 projects/agentic-devops-responder/responder.py --incident sample-503.json --dry-run
```

## Contact

avinashnandhyala12@gmail.com · GitHub: avinash-nandhyala · LinkedIn above.
