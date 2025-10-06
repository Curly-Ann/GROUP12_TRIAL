from django.shortcuts import render

# Create your views here.
@login_required # type: ignore
def projects_list_view(request):
    """Display list of all projects with their tasks"""
    
    try:
        # Get auth token from session
        token = request.session.get('auth_token')
        
        # Fetch projects from API
        projects_response = request.get(
            'http://localhost:8000/api/projects/',
            headers={'Authorization': f'Bearer {token}'}
        )
        
        # Fetch all tasks from API
        tasks_response = request.get(
            'http://localhost:8000/api/tasks/',
            headers={'Authorization': f'Bearer {token}'}
        )
        
        if projects_response.status_code == 200 and tasks_response.status_code == 200:
            projects = projects_response.json()
            tasks = tasks_response.json()
            
            # Group tasks by project
            for project in projects:
                project['tasks'] = [
                    task for task in tasks 
                    if task.get('project_id') == project['id']
                ]
            
            return render(request, 'projects.html', {
                'projects': projects
            })
        else:
            return render(request, 'projects.html', {
                'error': 'Failed to load projects',
                'projects': []
            })
    except Exception as e:
        return render(request, 'projects.html', {
            'error': str(e),
            'projects': []
        })