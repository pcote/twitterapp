$(function(){

    var getTweetsButtonClick = function(e){
    };

    $("#usernameTF").focus();
    $("#getTweetsButton").click(getTweetsButtonClick);

    var template = Handlebars.compile($("#cardListTemplate").html());

    var dummyData = {"tweets": [
        {username: "raz0rfist",
         tweetMessage: "I'd hate for an unelected judge to conduct himself as a sultan",
         tweetDate: "2017, Feb 5"},
        {username: "raz0rfist",
         tweetMessage: "Just in case being ripped off twice in a month didn't turn me off quite enough...",
         tweetDate: "2017, Feb 5"},
        {username: "raz0rfist",
         tweetMessage: "If the authoritarian left want to 'credit' anyone for the rise of the so-called 'Alt-Right', they should invest in reflective surfaces.",
         tweetDate: "2017, Feb 5"}
    ]};

    var renderedText = template(dummyData);
    var renderedDom = $(renderedText);
    $("#cardListArea").append(renderedDom);
});