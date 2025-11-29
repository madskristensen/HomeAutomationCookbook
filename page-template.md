---
layout: default
title: [REPLACE: Specific Action] - [REPLACE: Category] Automation Guide
description: [REPLACE: 140-160 character description of automation and benefits]
keywords: [REPLACE: keyword1, keyword2, keyword3, keyword4, keyword5, keyword6, keyword7, keyword8]
---

# [REPLACE: Main Action Title]

[REPLACE: 2-3 sentence introduction explaining the problem this solves and why it's valuable]

## Use Cases

* **[REPLACE: Scenario 1]** - [Brief description]
* **[REPLACE: Scenario 2]** - [Brief description]
* **[REPLACE: Scenario 3]** - [Brief description]
* **[REPLACE: Scenario 4]** - [Brief description]
* **[REPLACE: Scenario 5]** - [Brief description]

## Products Needed

### Essential

* **[REPLACE: Device Type 1]** - [Description]
  - Popular brands: [Brand 1, Brand 2, Brand 3]
  - Key features: [What to look for]
  
* **[REPLACE: Device Type 2]** - [Description]
  - Options: [List examples]

### Optional Enhancements

* **[REPLACE: Optional Device]** - [What it adds to automation]

## Basic Automation Setup

### Triggers
* [REPLACE: Primary trigger]
* OR [REPLACE: Alternative trigger]

### Conditions (Optional)
* **[REPLACE: Condition type]:** [When this should apply]
* **[REPLACE: Condition type]:** [Additional constraint]

### Actions
* [REPLACE: First action]
* [REPLACE: Second action]
* Optional: [REPLACE: Optional action]

## Platform-Specific Examples

### Home Assistant

```yaml
automation:
  - alias: "[REPLACE: Automation Name]"
    description: "[REPLACE: Brief description]"
    trigger:
      - platform: [REPLACE: trigger_type]
        entity_id: [REPLACE: entity.name]
        to: '[REPLACE: state]'
    condition:
      - condition: [REPLACE: condition_type]
        entity_id: [REPLACE: entity.name]
        state: '[REPLACE: state]'
    action:
      - service: [REPLACE: service.name]
        target:
          entity_id: [REPLACE: entity.name]
        data:
          [REPLACE: parameter]: [REPLACE: value]
```

### SmartThings

Create routine:
1. **IF** [REPLACE: Trigger description]
2. **AND** [REPLACE: Condition if needed]
3. **THEN** [REPLACE: Action description]

### Apple HomeKit

1. Create automation in Home app
2. **When:** [REPLACE: Trigger]
3. **Conditions:** [REPLACE: Optional conditions]
4. **Do:** [REPLACE: Actions]

### Alexa

Create routine:
1. **When:** [REPLACE: Trigger]
2. **Add condition:** [REPLACE: Optional condition]
3. **Action:** [REPLACE: What happens]

### Google Home

Create automation:
1. **Starter:** [REPLACE: Trigger]
2. **Condition:** [REPLACE: Optional]
3. **Action:** [REPLACE: What happens]

## Advanced Features

### [REPLACE: Feature Name]

[REPLACE: Description of advanced feature and how to implement it]

```yaml
# Example code if applicable
[REPLACE: code example]
```

### [REPLACE: Another Feature]

[REPLACE: Description and implementation]

## Troubleshooting

### Issue: [REPLACE: Common Problem]

**Causes:**
- [REPLACE: Cause 1]
- [REPLACE: Cause 2]
- [REPLACE: Cause 3]

**Solutions:**
✅ [REPLACE: Solution 1]
✅ [REPLACE: Solution 2]
✅ [REPLACE: Solution 3]

### Issue: [REPLACE: Another Problem]

**Check:**
- ✅ [REPLACE: Verification item]
- ✅ [REPLACE: Verification item]
- ✅ [REPLACE: Verification item]

**Fix:**
- [REPLACE: Step-by-step solution]

## SEO Keywords

[REPLACE: Natural sentence containing main keywords for better SEO]

---

**Related Automations:**
- [REPLACE: Related Title 1](/automation/category/page-name/)
- [REPLACE: Related Title 2](/automation/category/page-name/)

[← Back to [REPLACE: Category] Automations](/automation/category/) | [View All Automations →](/automation/)
