function addPricingRow(e) {
    e.preventDefault();

    const pricingRow = e.target.parentNode.parentNode.parentNode;

    const newPricingRow = pricingRow.cloneNode(true);

    const newdelbtn = newPricingRow.querySelector('#div_sil_button');
    if (newdelbtn) {
        newdelbtn.style.display = 'block'; 
        newdelbtn.id = 'div_sil_button';
    }

    newPricingRow.querySelectorAll('input').forEach((input) => {
        if (input.type === 'number' || input.type === 'text') {
            input.value = ''; 
        }
    });

    newPricingRow.querySelectorAll('select').forEach((select) => {
        select.selectedIndex = 0; 
    });

    const new_min = newPricingRow.querySelector('#id_min_people');
    new_min.removeAttribute('readonly');

    const old_max = pricingRow.querySelector('#id_max_people');
    old_max.setAttribute('required','true');

    const old_max_label = pricingRow.querySelector('#max_span');
    old_max_label.style.display = 'inline';

    const new_max = newPricingRow.querySelector('#id_max_people');
    new_max.removeAttribute('required');

    const new_max_label = newPricingRow.querySelector('#max_span');
    new_max_label.style.display = 'none';

    const delbtn = pricingRow.querySelector('#div_sil_button');
    if (delbtn) {
        delbtn.style.display = 'none';
    }


    pricingRow.parentNode.insertBefore(newPricingRow, pricingRow.nextSibling);

    e.target.parentNode.parentNode.style.display = 'none';
}

function removePricingRow(e) {
    e.preventDefault();

    row = e.target.parentNode.parentNode.parentNode;

    const previousRow = row.previousElementSibling;

    previousRow.querySelectorAll('button').forEach((element) => {
        element.parentNode.parentNode.style.display = 'block';
    })

    const prev_max = previousRow.querySelector('#id_max_people');
    prev_max.removeAttribute('required');

    const prev_max_label = previousRow.querySelector('#max_span');
    prev_max_label.style.display = 'none';

    row.remove();
    
    const all_pricing = document.querySelectorAll('#pricing_row');
    if (all_pricing.length === 1) {
        const silbtn = previousRow.querySelector('#div_sil_button');
        silbtn.style.display = 'none';
    }
}

function handleMinChange(inputElement) {
    const row = inputElement.parentNode.parentNode.parentNode;
    const max = row.querySelector('#id_max_people')

    if (parseInt(inputElement.value) >= parseInt(max.value)) {
        inputElement.value = parseInt(max.value) - 1
        alert('Son değişiklikleriniz maksimum yolcu sayısına göre güncellendi.');
    }

    const prev_row = inputElement.parentNode.parentNode.parentNode.previousElementSibling;
    const prev_max = prev_row.querySelector('#id_max_people')

    if (parseInt(inputElement.value) <= parseInt(prev_max.value)) {
        inputElement.value = parseInt(prev_max.value) + 1
        alert('Son yolcu paketiniz önceki fiyatlandırmadaki yolcu sayısına göre güncellendi.');
    }
    
}

function handleMaxChange(inputElement) {
    const row = inputElement.parentNode.parentNode.parentNode;
    const min = row.querySelector('#id_min_people')

    if (parseInt(inputElement.value) <= parseInt(min.value)) {
        inputElement.value = parseInt(min.value) + 1
        alert('Son değişiklikleriniz maksimum yolcu sayısına göre güncellendi.');
    }

    const next_row = inputElement.parentNode.parentNode.parentNode.nextElementSibling;
    const next_max = next_row.querySelector('#id_min_people')
    
    if (parseInt(inputElement.value) >= parseInt(next_max.value)) {
        inputElement.value = parseInt(next_max.value) - 1
        alert('Yolcu paketiniz diğer fiyatlandırmadaki yolcu sayısına göre güncellendi.');
    }
    
}