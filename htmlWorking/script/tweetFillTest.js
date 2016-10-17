function fillInTweets(){    
    //should be provided by the server side stuff probably.
    var marshaList = ["voteMarsha", "Rep.MarshaBlackburn", "Honored to serve the people of the 7th District", "http://pbs.twimg.com/profile_images/349460776/MWBConvention_normal.jpg"];
    var ASlist = ["RepAdamSmith", "Rep. Adam Smith", "Proudly serving Washington State's 9th District. Ranking Member of the House Armed Services Committee @HASCDemocrats", "http://pbs.twimg.com/profile_images/1554717159/Adam_Official_Photo_small_2009_normal.JPG"];
    var MQlist = ["RepMikeQuigley", "Mike Quigley", "#IL05 Congressman, House Appropriator, member of Intel Committee, amateur hockey player & hopeful Cubs fan http://t.co/zL9fkzy188  http://t.co/FMe57EKfsC", "http://pbs.twimg.com/profile_images/722431331184066565/LCCfS3fM_normal.jpg"];
    var profList = [marshaList, ASlist, MQlist];
    var numProfiles = profList.length;
    var tw_profiles = "";
    
    for (var i = 0; i < numProfiles; i++){
        tw_profiles += "<div class='row tweetRow'>";
        tw_profiles += "<div class='col-xs-10 col-xs-offset-1 profileSect col-md-6 col-md-offset-3'>";  //need col-md-something to figure out the best way to make pretty on bigger screens
        tw_profiles += "<img class='twPic' src='"+profList[i][3] + "'>";
        tw_profiles += "<a href='http://www.twitter.com/" + profList[i][0] + "' target='_blank' class='twitterName'>" + profList[i][1] + "</a>";
        tw_profiles += " <span class='handleName'><a href='http://www.twitter.com/" + profList[i][0] +"' target='_blank'>@" + profList[i][0] + "</a></span>";
        tw_profiles += "<p class='profDesc'>" + profList[i][2] + "</p>";
        tw_profiles += "</div>"; //column
        tw_profiles +="</div>"; //row
    }
    $("#shList").append(tw_profiles); //for easiest handling, this should be done with some sort of try situation so we can do both fillable areas in one go, even though they have different ID names
}


$(document).ready(function(){
    fillInTweets();
});