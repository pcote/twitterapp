$(function(){

    var getTweetsSuccess = function(data){
        var template = Handlebars.compile($("#cardListTemplate").html());
        var renderedText = template(data);
        var renderedDom = $(renderedText);
        $("#cardListArea").empty();
        $("#cardListArea").append(renderedDom);
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

    $("#usernameTF").focus();
    $("#getTweetsButton").click(getTweetsButtonClick);


});