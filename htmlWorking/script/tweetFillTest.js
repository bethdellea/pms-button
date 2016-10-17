function fillInTweets(){    
    var numProfiles = 2;
    var marshaList = ["voteMarsha", "Rep.MarshaBlackburn", "Honored to serve the people of the 7th District", "http://pbs.twimg.com/profile_images/349460776/MWBConvention_normal.jpg"];
    var ASlist = ["RepAdamSmith", "Rep. Adam Smith", "Proudly serving Washington State's 9th District. Ranking Member of the House Armed Services Committee @HASCDemocrats", "http://pbs.twimg.com/profile_images/1554717159/Adam_Official_Photo_small_2009_normal.JPG"];
    var profList = [marshaList, ASlist];
    var tw_profiles = "";
    for (var i = 0; i < 2; i++){
        tw_profiles += "<div class='row'>";
        tw_profiles += "<div class='col-xs-10 col-xs-offset-1 profileSect'>";
        tw_profiles += "<img class='twPic' src='"+profList[i][3] + "'>";
        tw_profiles += "<a href='twitter.com/" + profList[i][0] + "' target='_blank' class='twitterName'>" + profList[i][1] + "</a>";
        tw_profiles += "<span class='handleName'><a href='twitter.com/" + profList[i][0] + "target='_blank'>@" + profList[i][0] + "</a></span>";
        tw_profiles += "<p class='profDesc'>" + profList[i][2] + "</p>";
        tw_profiles += "</div>"; //column
        tw_profiles +="</div>"; //row
    }
    $("#shList").append(tw_profiles);
}


$(document).ready(function(){
    fillInTweets();
});