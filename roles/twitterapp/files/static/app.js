$(function(){

    var getDraggedOb = function(evt){
        var obId = "#" + evt.originalEvent.dataTransfer.getData("text");
        var ob = $(obId);
        return ob;
    };

    var getTargetOb = function(evt){
        var obId = "#" + evt.originalEvent.target.id
        var ob = $(obId);
        return ob;
    };

    // drag drop stuff
    var dragstartHandler = function(evt){
        var draggedObId = evt.originalEvent.target.id;
        evt.originalEvent.dataTransfer.setData("text", draggedObId);
        console.log("drag start ...");
    };

    var dragoverHandler = function(evt){
        evt.preventDefault();
    };


    var dropHandler = function(evt){
        var droppedItem = getDraggedOb(evt);
        var dropzone = getTargetOb(evt);
        droppedItem.insertBefore(dropzone);
        dropzone.css("background-color", "white");
    };

    var dragenterHandler = function(evt){
        var target = getTargetOb(evt);
        target.css("background-color", "#eeeeee");
    };

    var dragleaveHandler = function(evt){
        var target = getTargetOb(evt);
        target.css("background-color", "white");
    };

    var getTweetsSuccess = function(data){
        var template = Handlebars.compile($("#cardListTemplate").html());
        var renderedText = template(data);
        var renderedDom = $(renderedText);
        $("#cardListArea").empty();
        $("#cardListArea").append(renderedDom);
        $(".tweetCard").on("dragstart", dragstartHandler);
        $(".tweetCard").on("dragover", dragoverHandler);
        $(".tweetCard").on("drop", dropHandler);
        $(".tweetCard").on("dragenter", dragenterHandler);
        $(".tweetCard").on("dragleave", dragleaveHandler);
    };

    var getTweetsFailure = function(res){
        alert("nope, bombed");
    };

    var getTweetsButtonClick = function(e){
        var url = "/tweets?";
        var tweetHandles = $("#usernameTF").val().split(",");

        var wordFilter = function(w){
            if(w.search(/\w+/) >= 0){
                return true;
            }
            else {
                return false;
            }
        };

        var wordTrimmer = function(w){
            return w.trim();
        };

        tweetHandles = tweetHandles.filter(wordFilter);
        tweetHandles = tweetHandles.map(wordTrimmer);
        tweetHandles = tweetHandles.map(function(handle){
            return "tweethandle=" + handle;
        });

        tweetHandles = tweetHandles.join("&");

        var maxTweets = "maxtweets=" + $("#maxTweetsSelect").val();
        var baseUrl = "/tweets";
        var fullUrl = baseUrl + "?" + tweetHandles + "&" + maxTweets;

        var req = {
            url: fullUrl,
            method: "get"
        };

        var promise = $.ajax(req);
        promise.then(getTweetsSuccess, getTweetsFailure);
    };


    var getTweetsForPosition = function(position){
        var latitude = position.coords.latitude;
        var longitude = position.coords.longitude;
        var radius = $("#radiusSelect").val();

        var url = "/tweetsinarea";
        url = url + "?latitude=" + latitude + "&longitude=" + longitude + "&radius=" + radius;

        var promise = $.get(url);
        promise.then(getTweetsSuccess, getTweetsFailure);
    };

    var getLocalsClick = function(evt){
        console.log("getLocalsClick function");
        navigator.geolocation.getCurrentPosition(getTweetsForPosition);
    };

    $("#usernameTF").focus();
    $("#getTweetsButton").click(getTweetsButtonClick);

    $("#btnGetLocals").click(getLocalsClick);


});