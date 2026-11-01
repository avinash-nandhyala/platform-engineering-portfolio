# Service Mesh Troubleshooting Toolkit — Generic Recreation

## Problem it solves
An app returns 503s or SSL handshake errors, but its pods, endpoints, and routes all look healthy. The missing piece is often outside the app: traffic passes through a service mesh gateway, and the gateway hostname or certificate was not updated when the route moved.

This toolkit makes that check explicit, before guessing at app code.

## Intake first — ask before you run anything
1. Does traffic pass through a service mesh gateway? (If yes, gateway checks come early. If no, skip them.)
2. What is the exact error, URL, and time window?
3. What changed recently — migration, route change, certificate rotation?
4. Is it one app, one namespace, or many?

Different issues need different paths. This is not a blind run-every-command list.

## What to run, in order

```bash
# 1. App health
oc get pods -n <namespace>
oc get endpoints <service> -n <namespace>

# 2. Route (OpenShift)
oc get route <route> -n <namespace> -o yaml

# 3. Gateway — only if traffic uses a mesh gateway
oc get gateway -n <mesh-namespace>
oc get gateway <gateway-name> -n <mesh-namespace> -o yaml
# Check: does the gateway list the hostname the client is actually calling?

# 4. Certificates
./check-gateway.sh <namespace> <gateway-name>
# Checks gateway hosts against route hosts, and lists certificate secrets referenced.
```

See `check-gateway.sh` — it prints the comparison, it does not change anything. All commands are read-only.

## Lesson, generalised
When apps sit behind a mesh gateway, update gateway hostnames and gateway certificates alongside routes during any migration. Missing gateway hosts/certs cause 503s and SSL errors even when routes, endpoints, and pods are healthy.

No company cluster names, app names, or internal data are used here. Replace `<namespace>`, `<service>`, and `<gateway-name>` with your own values.
