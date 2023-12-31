// Load the modal content when the button is clicked
$("button.card").click(function() {
    $("input[name=name]#id_name").val("");
    $("input[name=date]#id_date").val("");
    $("select[name=color]").val("yellow").change();
    $("textarea[name=description]").val("");
});

// Load the modal content when the button is clicked
$(".content[id=event]").click(function() {
    t = $(this).text().split("\n");
    s = [];
    for(text in t){
       s.push(t[text].trim()) 
    }

    var parts = (s[1] + "T" + s.slice(-3)[0].split(" ")[1]).split("T");
    var dateParts = parts[0].split("/");
    var timeParts = parts[1].split(":");


    color = $(this).parent().attr('data-color')
    
    description = ""

    for (var i = 3; i < s.length; i++) {
        // Iterate over numeric indexes from 0 to 5, as everyone expects.
        if(!s[i].includes("Hour:")){
            if(s[i] !== "")
                description += s[i] + "\n";
        }
        else{
            break;
        }
    }

    // Format the date and time string in the expected format "yyyy-MM-ddThh:mm"
    var formattedDateTime = `${dateParts[2]}-${dateParts[1]}-${dateParts[0]}T${timeParts[0]}:${timeParts[1]}`;
    $("input[name=name]#id_name").val(s[2]);
    $("input[name=date]#id_date").val(formattedDateTime);
    $("select[name=color]").val(color).change();
    $("textarea[name=description]").val(description);
    $("span[name=id]").val(s.slice(-2)[0]);
});