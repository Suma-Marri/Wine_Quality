// Using d3.select to grab inputs and store them as Variables.
var input1 = d3.select("#input1")
var input2 = d3.select("#input2")
var input3 = d3.select("#input3")
var input4 = d3.select("#input4")
var input5 = d3.select("#input5")
var input6 = d3.select("#input6")
var input7 = d3.select("#input7")
var input8 = d3.select("#input8")
var input9 = d3.select("#input9")
var input10 = d3.select("#input10")
var input11 = d3.select("#input11")

// Select the button
var button = d3.select("#button");

// Create event handlers
button.on("click", runEnter);

// Complete the event handler function for the form
function runEnter() {
    // Get the value properties of the input elements
    var inputValue1 = input1.property("value")
    var inputValue2 = input2.property("value")
    var inputValue3 = input3.property("value")
    var inputValue4 = input4.property("value")
    var inputValue5 = input5.property("value")
    var inputValue6 = input6.property("value")
    var inputValue7 = input7.property("value")
    var inputValue8 = input8.property("value")
    var inputValue9 = input9.property("value")
    var inputValue10 = input10.property("value")
    var inputValue11 = input11.property("value")

    var user_wine = [inputValue1, inputValue2,inputValue3, inputValue4, inputValue5, inputValue6, inputValue7, inputValue8, inputValue9, inputValue10, inputValue11]
    console.log("user_wine: ", user_wine)
}
