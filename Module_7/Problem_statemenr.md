# Module 7 Capstone: GitHub Copilot Enterprise Policy & Role-Based Access Simulation

## Objective
You are simulating the responsibilities of a **GitHub Copilot Enterprise Admin** for the fictional company `InnovaWorks`.  
You must:
1. Create enterprise-wide Copilot policy configurations.
2. Implement and enforce role-based access rules.
3. Simulate license allocation under seat constraints.
4. Apply repository allow/block lists and content exclusion rules.
5. Generate telemetry and prompt audit logs.
6. Document a formal role-change workflow.

## Context
Your organization has these roles:
1. **Org_Admin** — Full Copilot access, manages policies.
2. **Senior_Dev** — Copilot allowed in all repos *except* sensitive repos.
3. **Junior_Dev** — Copilot allowed only in sandbox/training repos.
4. **External_Contractor** — Copilot disabled entirely.

### Rules:
- Sensitive repos: `finance-reports`, `security-audit`.
- All roles must exclude `/private/` from Copilot training.
- 50 Copilot licenses are available, allocation priority:  
  `Org_Admin > Senior_Dev > Junior_Dev > External_Contractor`.
- Telemetry & prompt audit are enabled for all usage.
- Only **Org_Admin** can approve role changes.

---

## Deliverables
You must produce the following files:

1. **`policy_config.yaml`**  
   Enterprise Copilot policy configuration:
   - Allowed/blocked repos for each role.
   - Content exclusions.
   - Global telemetry & prompt audit settings.

2. **`role_access_matrix.json`**  
   JSON defining Copilot enablement, allowed repos, blocked repos, and exclusions for each role.

3. **`license_allocation.yaml`**  
   YAML showing number of seats per role and remaining seats.

4. **`telemetry_log_sample.md`**  
   Markdown table with at least **2 entries**:  
   - Allowed prompt by a permitted role/repo.  
   - Blocked prompt attempt by a restricted role/repo.

5. **`role_change_request.md`**  
   Markdown form for requesting a role upgrade/downgrade, including approvals.

---

## Steps
1. Define your **policy_config.yaml** using Copilot.
2. Generate the **role_access_matrix.json** based on the policy config.
3. Allocate seats in **license_allocation.yaml** using constraints.
4. Simulate **telemetry_log_sample.md** entries.
5. Create **role_change_request.md** workflow form.

---

#
