def find_task_by_id(tasks, task_id):
    """
    Find a task by its ID in the list of tasks
    
    Args:
        tasks: List of task objects
        task_id: ID of the task to find
        
    Returns:
        Task object if found, None otherwise
    """
    for task in tasks:
        if task.id == task_id:
            return task
    return None