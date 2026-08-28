# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: QualityLog
def get_next_action_recommendation(log):
    """Recommend next action based on current quality log state."""
    if not log or not log.get('entries'):
        return "Start by adding the first quality check to your log."

    entries = log['entries']
    last_entry = entries[-1]

    if last_entry['status'] == 'open':
        if last_entry.get('has_solution'):
            return "Review the solution, then mark the check as resolved or move to next check."
        else:
            return "Decide: assign a responsible person and add a solution, or escalate the check."

    if last_entry['status'] == 'resolved':
        resolved_count = sum(1 for e in entries if e['status'] == 'resolved')
        total = len(entries)
        if resolved_count >= total:
            return "All checks are resolved. Consider archiving the log or starting a new cycle."
        else:
            return "Continue with the next unresolved check in the log."

    if last_entry['status'] == 'rejected':
        return "Re-evaluate the rejected check or mark it as resolved if the rejection was intentional."

    return "Check the log for any unresolved entries and address them."
