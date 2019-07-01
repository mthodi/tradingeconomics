$(document).ready(function(){
    $('a[data-toggle="tab"]').on('shown.bs.tab', function(e){
        var currentTab = $(e.target).text(); // get current tab
        var LastTab = $(e.relatedTarget).text(); // get last tab
       console.log("something changed")
    });
});