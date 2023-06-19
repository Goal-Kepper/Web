// Получение списка новостей с сервера
function getNews() {
  var xhr = new XMLHttpRequest();
  xhr.open('GET', '/news', true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      var news = JSON.parse(xhr.responseText);
      var list = document.getElementById('news-list');
      var html = '';
      for (var i = 0; i < news.length; i++) {
        html += '<li><h2>' + news[i].name + '</h2><p>' + news[i].text + '</p><button onclick="editNews(' + news[i].id + ')">Редактировать</button><button onclick="deleteNews(' + news[i].id + ')">Удалить</button></li>';
      }
      list.innerHTML = html;
    }
  };
  xhr.send();
}

// Добавление новости на сервер
function addNews() {
  var name = document.getElementById('news-name').value;
  var text = document.getElementById('news-text').value;
  var xhr = new XMLHttpRequest();
  xhr.open('POST', '/news', true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      getNews(); // Обновляем список новостей после добавления
    }
  };
  document.getElementById('news-name').value = "";
  document.getElementById('news-text').value = "";
  xhr.send(JSON.stringify({name: name, text: text}));
}

// Редактирование новости на сервере
function editNews(id) {
  var name = prompt('Введите новый заголовок:');
  var text = prompt('Введите новый текст:');
  var xhr = new XMLHttpRequest();
  xhr.open('PUT', '/news/' + id, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      getNews(); // Обновляем список новостей после редактирования
    }
  };
  xhr.send(JSON.stringify({name: name, text: text}));
}

// Удаление новости на сервере
function deleteNews(id) {
  var xhr = new XMLHttpRequest();
  xhr.open('DELETE', '/news/' + id, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
      getNews(); // Обновляем список новостей после удаления
    }
  };
  xhr.send();
}

// Обработка отправки формы для добавления новости
document.getElementById('add-news-form').addEventListener('submit', function(event) {
  event.preventDefault(); // Отменяем стандартное поведение формы
  addNews();
});

window.onload = function() {
  getNews();
};