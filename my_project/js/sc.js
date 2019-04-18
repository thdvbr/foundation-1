SC.initialize({
    client_id: "d4ab52d80ed2e7790c3a243495b30093",
    //    redirect_uri: "https://developers.soundcloud.com/callback.html",
});

SC.stream("/tracks/556357263").then(function(player){
    player.play();
});

