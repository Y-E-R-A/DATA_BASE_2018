(function() {

    var app = angular.module('AppChat',['ngRoute']);

    app.config(['$routeProvider', '$locationProvider', function ($routeProvider, $locationProvider, $location) {
        $routeProvider.when('/chat', {
            templateUrl: 'pages/chat.html',
            controller: 'ChatController',
            controllerAs : 'chatCtrl'
        }).when('/gchat/:uid/:gid', {
            templateUrl: 'pages/gchat.html',
            controller: 'GChatController',
            controllerAs : 'gchatCtrl/:uid/:gid'
        }).when('/messagerating/:mid', {
            templateUrl: 'pages/messagerating.html',
            controller: 'MessageRatingController',
            controllerAs : 'messageRatingCtrl'
        }).when('/signup', {
            templateUrl: 'pages/signup.html',
            controller: 'SignUpController',
            controllerAs : 'signupCtrl'
        }).when('/group/:uid', {
            templateUrl: 'pages/group.html',
            controller: 'GroupController',
            controllerAs : 'groupCtrl'
        }).when('/login', {
            templateUrl: 'pages/login.html',
            controller: 'LoginController',
            controllerAs : 'loginCtrl'
        }).when('/newgroup/:uid', {
            templateUrl: 'pages/newgroup.html',
            controller: 'NewGroupController',
            controllerAs : 'newGroupCtrl'
        }).when('/addparticipant/:uid', {
            templateUrl: 'pages/addparticipant.html',
            controller: 'AddParticipantController',
            controllerAs : 'addParticipantCtrl'
        }).otherwise({
            redirectTo: '/login'
        });
    }]);

})();