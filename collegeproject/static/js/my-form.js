const departmenttSelect = document.querySelector('#id_department');
const courseSelect = document.querySelector('#id_course');


departmenttSelect.addEventListener('change', () => {
  // Reset the course dropdown menus
  courseSelect.innerHTML = '<option value="">--------</option>';


  // Populate the course dropdown menu based on the selected department
  if (departmentSelect.value === 'commerce') {
    courseSelect.innerHTML += '<option value="BCOM">BCOM</option><option value="BBA">BBA</option><option value="CA">CA</option><option value="BBM">BBM</option>';
  } else if (departmentSelect.value === 'it') {
    courseSelect.innerHTML += '<option value="">China</option><option value="india">India</option><option value="japan">Japan</option><option value="BCOM">BCOM</option><option value="BBA">BBA</option>';
  } else if (departmentSelect.value === 'social') {
    courseSelect.innerHTML += '<option value="france">France</option><option value="germany">Germany</option><option value="united-kingdom">United Kingdom</option><option value="BCOM">BCOM</option><option value="BBA">BBA</option>'';
  }
  } else if (departmentSelect.value === 'science') {
    courseSelect.innerHTML += '<option value="france">France</option><option value="germany">Germany</option><option value="united-kingdom">United Kingdom</option><option value="BCOM">BCOM</option><option value="BBA">BBA</option>'';
  }
  } else if (departmentSelect.value === 'arts') {
    courseSelect.innerHTML += '<option value="france">France</option><option value="germany">Germany</option><option value="united-kingdom">United Kingdom</option><option value="BCOM">BCOM</option><option value="BBA">BBA</option>'';
  }
  } else if (departmentSelect.value === 'literature') {
    courseSelect.innerHTML += '<option value="france">France</option><option value="germany">Germany</option><option value="united-kingdom">United Kingdom</option>'<option value="BCOM">BCOM</option><option value="BBA">BBA</option>'';
  }
});

countrySelect.addEventListener('change', () => {
  // Reset the city dropdown menu
  citySelect.innerHTML = '<option value="">--------</option>';

  // Populate the city dropdown menu based on the selected country
  if (countrySelect.value === 'egypt') {
    citySelect.innerHTML += '<option value="cairo">Cairo</option><option value="alexandria">Alexandria</option>';
  } else if (countrySelect.value === 'south-africa') {
    citySelect.innerHTML += '<option value="johannesburg">Johannesburg</option><option value="cape-town
