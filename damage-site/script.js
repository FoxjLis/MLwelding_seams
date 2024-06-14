// const input = document.querySelector('.input_file');
// const results = document.querySelector('.results-container');
// const instructions = document.querySelector('.instructions');


// input.addEventListener('change', async function() {
//   const file = input.files[0]; 
//   const formData = new FormData(); 
//   results.innerHTML = `<div style = 'color: black; font-size: 20px; text-align: center;' class="claster-wrapper">
//       Подождите, анализ файла займет примерно 30 секунд
//     </div>`
//   instructions.innerHTML = `<p>Подождите, анализ файла займет примерно 30 секунд</p>`
//   formData.append('file', file); 
//     fetch('https://dockerr.containers.cloud.ru/whatsimplant', {
//       method: 'POST',
//       body: formData
//     }).then(function(response) {
//       return response.json()
      
//     }).then(function(res) {
//       let path = res.image_path
//       let implant = res.results[0].name
//       let count = res.results.length
//       if (implant === 'ITI') {
//         results.innerHTML = `
//         <div class="claster-wrapper">
//             Ваш <br>
//             результат
//         </div>
//         <div class="results">
//             <div class="result">
//                 <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
//             </div> 
//             <div class="description">
//                 <p>Вид: <span>ITI Straumann</span></p>
//                 <p>Количество: <span>${count}</span></p>
//                 <p>Описание: <span>Имплантационная система Straumann разработана для простоты и свободы выбора: одна система с одним набором, который можно использовать по всем показаниям, и уникальный ассортимент различных материалов и поверхностей, включая такие передовые технологии, как Roxolid и SLActive</span></p>
//             </div>
//         </div>`
//       }
//       if (implant === 'Bego') {
//         results.innerHTML = `
//         <div class="claster-wrapper">
//             Ваш <br>
//             результат
//         </div>
//         <div class="results">
//             <div class="result">
//                 <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
//             </div> 
//             <div class="description">
//                 <p>Вид: <span>Bego Semados</span></p>
//                 <p>Количество: <span>${count}</span></p>
//                 <p>Описание: <span>Bego Semados (Бего Семадос) – это европейская компания с богатой историей и более чем тридцатилетним опытом в производстве зубных имплантатов. Среди ценностей компании высокое качество, инновации и научно обоснованные решения для стоматологической практики.</span></p>
//             </div>
//         </div>`
//       }
//       if (implant === 'Bicon') {
//         results.innerHTML = `
//         <div class="claster-wrapper">
//             Ваш <br>
//             результат
//         </div>
//         <div class="results">
//             <div class="result">
//                 <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
//             </div> 
//             <div class="description">
//                 <p>Вид: <span>Bicon</span></p>
//                 <p>Количество: <span>${count}</span></p>
//                 <p>Описание: <span>Клинически доказанный результат с 1985 года. Благодаря уникальному дизайну и революционным технологиям, система дентальных имплантатов Bicon не просто выдержала испытание временем, но продолжает занимать лидирующую позицию в имплантологии.</span></p>
//             </div>
//         </div>`
//       }
      
//     });
// });

const input = document.querySelector('.input_file');
const results = document.querySelector('.results-container');
const instructions = document.querySelector('.instructions');

input.addEventListener('change', async function() {
  const file = input.files[0]; 
  const formData = new FormData(); 
  results.innerHTML = `<div style='color: black; font-size: 20px; text-align: center;' class="claster-wrapper">
      Подождите, анализ файла займет примерно 30 секунд
    </div>`;
  instructions.innerHTML = `<p>Подождите, анализ файла займет примерно 30 секунд</p>`;
  formData.append('file', file);

  async function fetchData() {
    try {
      const response = await fetch('https://dockerr.containers.cloud.ru/whatsimplant', {
        method: 'POST',
        body: formData
      });
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      const res = await response.json();
      return res;
    } catch (error) {
      console.error('Fetching data failed:', error);
      return null;
    }
  }

  let res = null;
  while (res === null) {
    res = await fetchData();
  }

  let path = res.image_path;
  let implant = res.results[0].name;
  let count = res.results.length;

  if (implant === 'ITI') {
    results.innerHTML = `
    <div class="claster-wrapper">
        Ваш <br>
        результат
    </div>
    <div class="results">
        <div class="result">
            <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
        </div> 
        <div class="description">
            <p>Вид: <span>ITI Straumann</span></p>
            <p>Количество: <span>${count}</span></p>
            <p>Описание: <span>Имплантационная система Straumann разработана для простоты и свободы выбора: одна система с одним набором, который можно использовать по всем показаниям, и уникальный ассортимент различных материалов и поверхностей, включая такие передовые технологии, как Roxolid и SLActive</span></p>
        </div>
    </div>`;
  } else if (implant === 'Bego') {
    results.innerHTML = `
    <div class="claster-wrapper">
        Ваш <br>
        результат
    </div>
    <div class="results">
        <div class="result">
            <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
        </div> 
        <div class="description">
            <p>Вид: <span>Bego Semados</span></p>
            <p>Количество: <span>${count}</span></p>
            <p>Описание: <span>Bego Semados (Бего Семадос) – это европейская компания с богатой историей и более чем тридцатилетним опытом в производстве зубных имплантатов. Среди ценностей компании высокое качество, инновации и научно обоснованные решения для стоматологической практики.</span></p>
        </div>
    </div>`;
  } else if (implant === 'Bicon') {
    results.innerHTML = `
    <div class="claster-wrapper">
        Ваш <br>
        результат
    </div>
    <div class="results">
        <div class="result">
            <img src="${'https://dockerr.containers.cloud.ru/result/' + path}" alt="" srcset="">
        </div> 
        <div class="description">
            <p>Вид: <span>Bicon</span></p>
            <p>Количество: <span>${count}</span></p>
            <p>Описание: <span>Клинически доказанный результат с 1985 года. Благодаря уникальному дизайну и революционным технологиям, система дентальных имплантатов Bicon не просто выдержала испытание временем, но продолжает занимать лидирующую позицию в имплантологии.</span></p>
        </div>
    </div>`;
  }
});