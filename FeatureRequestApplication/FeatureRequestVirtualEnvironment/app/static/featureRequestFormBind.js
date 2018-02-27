// featureRequestFormBind.js consists javascript code which binds the form details entered in featureRequestForm.html using knockout js concept
// function FeatureRequestFormModel() consists of title, description, client, client priority,target date and product area fields
function FeatureRequestFormModel() {
    title = ko.observable(""),
        description = ko.observable(""),
        client = ko.observable(""),
        clientPriority = ko.observable(""),
        targetDate = ko.observable(""),
        productArea = ko.observable("")

};
// On form Submit onSubmit() function will send an ajax request which will post json data to url "http://127.0.0.1:5000/createFeatureRequest" 
onSubmit = function () {
    const path= 'http://127.0.0.1:5000/'
    $.ajax({
        data: JSON.stringify({
            title: title(),
            description: description(),
            client: client(),
            clientPriority: clientPriority(),
            targetDate: targetDate(),
            productArea: productArea()
        }),
        type: 'POST',
        url: path+'createFeatureRequest',
        contentType: 'application/json',
        success: function (result) {
            if(result == 'success') {
                document.getElementById('detailspage').click();
            }
            else if(result == 'Title name already exists.Please change name.') {
                alert('Title name already exists.Please change name.');
            }
            else { alert("Please Check your values and Submit"); }
        },
        error: function (error) {
            console.log(error);
            alert("Please check your details and resubmit" + error)
        }
    })
};
// knock out js has applyBindings property which will apply the binding of model on filling data
ko.applyBindings(new FeatureRequestFormModel());
//validation for limiting minimum date to tommorow
var today = new Date();
var dd = today.getDate()+1;
var mm = today.getMonth()+1; //January is 0!
var yyyy = today.getFullYear();
 if(dd<10){
        dd='0'+dd
    } 
    if(mm<10){
        mm='0'+mm
    } 

today = yyyy+'-'+mm+'-'+dd;
document.getElementById("targetDate").setAttribute("min", today);
