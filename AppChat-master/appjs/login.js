angular.module('AppChat').controller('LoginController', ['$http', '$log', '$scope', '$location',
    function($http, $log, $scope, $location) {
        
        var thisCtrl = this;
        console.log('hello 1')
        this.signUpRedirect = function(){
            console.log('hello 2')
        $scope.nowdate = Date();
           $location.url('/signup');
        };
        
        
        

}]);
