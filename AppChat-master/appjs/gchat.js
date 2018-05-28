angular.module('AppChat').controller('GChatController', ['$http', '$log', '$scope','$location', '$routeParams', 
    function($http, $log, $scope, $location, $routeParams) {
        var thisCtrl = this;
        $scope.nowdate = Date();
        
        this.messageList = [];
        this.counter  = 2;
        this.newText = "";
        
        
        this.loadMessages = function(){
            // Get the list of parts from the servers via REST API
            var uid = $routeParams.uid;
            var gid = $routeParams.gid;
            console.log("route userd Id: " +$routeParams.uid);
            console.log("route group Id: "+$routeParams.gid);
            
            
            console.log("userd Id: " +this.uid);
            console.log("group Id: "+this.gid);
           
        };
        
        this.postMsg = function(){
            
            var msg = thisCtrl.newText;
            // Need to figure out who I am
            var fecha = $scope.nowdate;
            var nextId = thisCtrl.counter++;
            thisCtrl.messageList.unshift({"uid": 1, "mid": nextId, "uName": "you", "mInfo": msg, "mDate": fecha, "like" : 0, "dislike" : 0});
            thisCtrl.newText = "";
        };
        this.messageRating = function (mid) {
            $location.url('/messagerating/' + mid);
        };
        
        this.loginRedirect= function(){
            $location.url('/login');
        };
        
        this.createGroupRedirect= function(){
            $location.url('/newgroup');
        };
            
        this.createAddParticipantRedirect= function(){
            $location.url('/addparticipant');
        };
        this.loadMessages();
}]);
