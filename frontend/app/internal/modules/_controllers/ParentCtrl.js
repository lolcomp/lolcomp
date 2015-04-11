angular.module('internal.controllers')
    .controller('ParentCtrl', ['$scope', 'LcComms',
        function ($scope, LcComms) {
            var cst;

            LcComms.call_ws("ws/cst_internal", {"test": null})
                .then(function (data) {
                    cst = $scope.cst = data;
                    initialize();
                })
                .catch(function (data) {
                    console.log(data, "catch")
                })
                
            var initialize = function () {
                $scope.static = {
                    get_url: function (resource) {
                        return cst.static_url + '/static/' + resource;
                    },
                    get_year: function () {
                        var date = new Date();
                        return date.getFullYear();
                    }
                }
                
                $scope.sidebar = {
                    model: [
                        {
                            label: 'Edit Champs',
                            url: 'internal/champs'
                        },{
                            label: 'Edit Rules',
                            url: 'internal/rules'
                        }
                    ]
                }
            }

        }]);