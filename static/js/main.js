var ingredient_set = new Set([]);
var ingredient_data
function get_ingre(ingre_val) {
    ingredient_set.add(ingre_val);
    let ingredients_list = "";
    ingredient_set.forEach (function(value) {
        ingredients_list += value + ",";
    })
    ingredients_list = ingredients_list.substring(0, ingredients_list.length-1);
    document.getElementById("ingredient_list").value = ingredients_list;
    console.log(ingredients_list)
    ingredient_data = ingredients_list
}

function clear_ingre(){
    document.getElementById("ingredient_list").value = "";
    ingredient_set = new Set([]);
    $("table tbody").empty();
}
