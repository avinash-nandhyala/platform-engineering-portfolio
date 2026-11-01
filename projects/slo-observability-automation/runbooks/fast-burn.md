# Fast burn runbook (sample)
1. Confirm the alert is real: check error rate and traffic, not just the alert.
2. Check recent deploys — roll back the last change if it correlates.
3. Check mesh gateway / certificate state if errors are 503 / SSL.
4. If budget will exhaust in hours, page the service owner and freeze non-essential deploys.
5. Write a postmortem with the burn timeline, even if you fix it fast.
