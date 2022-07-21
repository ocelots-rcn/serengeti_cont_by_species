let contVarData = {};
let contVarSpeciesList = null;

axios.get('../data/cont_var.json').then((response) => {
    contVarData = response.data;

    // Populate selection list
    let species = document.getElementById('ContVarSpecies');
    Object.keys(contVarData.species).sort().forEach( (val) => {
        let newOption = new Option(val, val);
        species.add(newOption,undefined);
    });

    contVarSpeciesList = new SlimSelect({
        select: '#ContVarSpecies'
    });

    // Needs a little delay
    setTimeout(() => {contVarSpeciesList.set(contVarData.groups['predator'])}, 500);
});

// Update graph when selections changes
const contVarPlot = () => {
    let variable = document.querySelector('input[name=contVarVariable]:checked').value;
    let format = document.querySelector('input[name=contVarFormat]:checked').value;
    let pdata = [];
    let selected = contVarSpeciesList.selected();

        if(selected.length > 0) {
            selected.forEach( (species) => {
                let plotd = {
                y: contVarData.species[species][variable],
                name: species,
                type: format
            };
            pdata.push(plotd);
        });
    }
    if(format === 'box') {
        if(variable.includes('Distance')){ 
            Plotly.newPlot('ContVarPlot', pdata, {yaxis: {title: variable, range: [0, 11000]}, xaxis: {title: 'Species'}}, {responsive: true});
        }
        else {
         Plotly.newPlot('ContVarPlot', pdata, {yaxis: {title: variable}, xaxis: {title: 'Species'}}, {responsive: true});
        }
    }
    else {
        Plotly.newPlot('ContVarPlot', pdata, {yaxis: {title: variable}, xaxis: {title: 'Frequency'}}, {responsive: true});
    }
}

const contVarClearList = () => {
    contVarSpeciesList.set([]);
}

// Quick load helper
const contVarQuickLoad = (key) => {
    contVarSpeciesList.set(contVarData.groups[key]);
}