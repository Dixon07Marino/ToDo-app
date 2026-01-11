const API_BASE = 'https://todo-app-production-745d.up.railway.app/';
const taskForm = document.getElementById('task-form');
const nameInput = document.getElementById('name');
const taskList = document.getElementById('task-list');

async function loadTasks() {
    try {
        const res = await fetch(API_BASE);
        if (!res.ok) throw new Error('Failed to load tasks');
        const tasks = await res.json();
        renderTasks(tasks);
    } catch (error) {
        console.error(error);
        alert('Error loading tasks. Check if backend is running.');
    }
}

function renderTasks(tasks) {
    taskList.innerHTML = '';
    tasks.forEach(task => {
        const li = document.createElement('li');
        li.className = 'bg-gray-800 p-4 rounded-lg shadow-lg flex items-center justify-between animate-fade-in';

        const nameSpan = document.createElement('span');
        nameSpan.textContent = task.name;
        nameSpan.className = 'text-white flex-1 cursor-pointer';
        nameSpan.onclick = () => editTask(task.id, nameSpan);

        const deleteBtn = document.createElement('button');
        deleteBtn.innerHTML = '<i data-lucide="trash-2"></i>';
        deleteBtn.className = 'text-red-500 hover:text-red-700';
        deleteBtn.onclick = () => deleteTask(task.id);

        li.append(nameSpan, deleteBtn);
        taskList.appendChild(li);
    });
    lucide.createIcons();
}

function editTask(id, span) {
    const input = document.createElement('input');
    input.value = span.textContent;
    input.className = 'bg-gray-800 text-white border border-cyan-500 rounded px-2 flex-1';
    input.onblur = () => saveEdit(id, input.value.trim(), span);
    input.onkeydown = (e) => { if (e.key === 'Enter') saveEdit(id, input.value.trim(), span); };
    span.replaceWith(input);
    input.focus();
}

function saveEdit(id, newName, originalSpan) {
    const finalName = newName || originalSpan.textContent;
    const newSpan = document.createElement('span');
    newSpan.textContent = finalName;
    newSpan.className = 'text-white flex-1 cursor-pointer';
    newSpan.onclick = () => editTask(id, newSpan);
    if (newName && newName !== originalSpan.textContent) {
        updateTask(id, { name: finalName });
    }
    // Replace input with span
    const input = document.querySelector(`input[value="${originalSpan.textContent}"]`) || input;
    input.replaceWith(newSpan);
}

async function addTask(task) {
    try {
        const res = await fetch(API_BASE, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(task)
        });
        if (!res.ok) throw new Error('Failed to add task');
        loadTasks();
    } catch (error) {
        console.error(error);
        alert('Error adding task');
    }
}

async function updateTask(id, updates) {
    try {
        const res = await fetch(`${API_BASE}/${id}`, {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(updates)
        });
        if (!res.ok) throw new Error('Failed to update task');
        loadTasks();
    } catch (error) {
        console.error(error);
        alert('Error updating task');
    }
}

async function deleteTask(id) {
    try {
        const res = await fetch(`${API_BASE}/${id}`, { method: 'DELETE' });
        if (!res.ok) throw new Error('Failed to delete task');
        loadTasks();
    } catch (error) {
        console.error(error);
        alert('Error deleting task');
    }
}

taskForm.onsubmit = (e) => {
    e.preventDefault();
    const name = nameInput.value.trim();
    if (name) {
        addTask({ name });
        nameInput.value = '';
    }
};

window.onload = loadTasks;
