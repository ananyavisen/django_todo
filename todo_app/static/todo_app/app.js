// =====================
// State
// =====================
let tasks = JSON.parse(localStorage.getItem('inklings-tasks') || '[]');
let currentFilter = 'all';
let editingId = null;

// =====================
// Persist
// =====================
function save() {
  localStorage.setItem('inklings-tasks', JSON.stringify(tasks));
}

// =====================
// Render
// =====================
function render() {
  const list = document.getElementById('taskList');
  const empty = document.getElementById('emptyState');
  const countLabel = document.getElementById('countLabel');

  const filtered = tasks.filter(t => {
    if (currentFilter === 'active') return !t.done;
    if (currentFilter === 'done')   return t.done;
    return true;
  });

  list.innerHTML = '';

  if (filtered.length === 0) {
    empty.classList.add('visible');
  } else {
    empty.classList.remove('visible');
    filtered.forEach((task, i) => {
      const li = createTaskEl(task, i);
      list.appendChild(li);
    });
  }

  const total  = tasks.length;
  const done   = tasks.filter(t => t.done).length;
  countLabel.textContent = `${total} task${total !== 1 ? 's' : ''} · ${done} done`;
}

function createTaskEl(task) {
  const li = document.createElement('li');
  li.className = 'task-item' + (task.done ? ' done' : '');
  li.dataset.id = task.id;

  li.innerHTML = `
    <label class="check-wrap">
      <input type="checkbox" ${task.done ? 'checked' : ''} onchange="toggleTask('${task.id}')"/>
      <div class="check-box"><span class="tick">✓</span></div>
    </label>
    <span class="task-text">${escapeHtml(task.text)}</span>
    <div class="task-actions">
      <button class="action-btn edit-btn" onclick="openEdit('${task.id}')" title="Edit">✏️</button>
      <button class="action-btn delete-btn" onclick="deleteTask('${task.id}')" title="Delete">✕</button>
    </div>
  `;

  return li;
}

// =====================
// CRUD
// =====================


