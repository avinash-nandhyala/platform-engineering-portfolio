# SAMPLE — 503 after a route move

Symptom: 503 errors, app pods healthy, endpoints healthy.
Root cause (generic pattern): traffic passes through a service mesh gateway, and the gateway hostname was not updated when the route moved.
Fix: add the called hostname to the gateway, verify the gateway certificate covers it, then re-test.
Lesson: update gateway hosts and certificates alongside routes during any migration.
