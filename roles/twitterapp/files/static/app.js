$(function(){

    var getTweetsButtonClick = function(e){
    };

    $("#usernameTF").focus();
    $("#getTweetsButton").click(getTweetsButtonClick);

    var template = Handlebars.compile($("#cardListTemplate").html());

    var dummyData = {"tweets": [
        {username: "chicken_b",
         tweetMessage: "#MySQL  group_concat function requires more trust in #Oracle than I care to give. A few extra lines from #python itertools mod is better.",
         tweetDate: "2017, Feb 5"},
        {username: "chicken_b",
         tweetMessage: "Brown field maintenance code is unavoidable. Even hobby projects get that way given enough time.",
         tweetDate: "2017, Feb 5"},
        {username: "chicken_b",
         tweetMessage: "New blog article: #jQuery Ideas That Help Me Memorize Really Big Numbers http://bit.ly/2dhO2jg ",
         tweetDate: "2017, Feb 5"}
    ]};

    var renderedText = template(dummyData);
    var renderedDom = $(renderedText);
    $("#cardListArea").append(renderedDom);
});