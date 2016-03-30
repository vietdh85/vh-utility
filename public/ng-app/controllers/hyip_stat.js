angular.module("app").controller("HyipStatCtrl", function($scope, $timeout, $interval, resources) {
		
	function createChart(chart_id, chart_name, unit1_name, unit2_name, data1, data2, data3){
		
		if(!data3) data3 = [];
		
		$('#' + chart_id).highcharts({
			chart: {
                zoomType: 'x'
            },
			colors: ['#6BAECF', '#f7a35c', '#46B31B'],
            title: {
                text: chart_name
            },
            subtitle: {
                text: ""
            },
            xAxis: {
                type: 'datetime'
            },
            yAxis: [
			{
                title: {
                    text: ''
                },
				min:0,
            },{
				title: {
                    text: ''
				},
				min:0,
			},{
				opposite: true,
				labels: {
					format: '{value}%',
				},
				title: {
                    text: 'Percent'
				},				
				min:0,
				max:100
			}],            
            plotOptions: {
                area: {           
					fillOpacity: 0.5,
                    marker: {
                        radius: 2
                    },
                    lineWidth: 1,
                    states: {
                        hover: {
                            lineWidth: 1
                        }
                    },
                    threshold: null
                }
            },

            series: [{
                type: 'area',
                name: unit1_name,
				data: data1,
				yAxis: 0
			},{
                type: 'area',
                name: unit2_name,
				data: data2,
				yAxis: 0
			},{
                type: 'line',
                name: 'Ratio',
				data: data3,
				yAxis: 2
			}]
		});
	}
	
	$scope.init = function(siteId){
		var params = {site_id:siteId};
		resources.hyips.listSiteStats(params).$promise.then(function(res) {
			//console.log("Updated Site", res);
			var list = res.data;
			var data_deposit = [];
			var data_withdraw = [];
			var data_withdraw_ratio = [];
			var data_total_acc = [];
			var data_active_acc = [];
			
			for(var i=0; i<list.length; i++){
				var time = Number(list[i].time) + 25200000;
				
				data_deposit[i] = []
				data_deposit[i].push(time);
				data_deposit[i].push(Number(list[i].total_deposit));
				
				data_withdraw[i] = []
				data_withdraw[i].push(time);
				data_withdraw[i].push(Number(list[i].total_withdraw));
				
				data_withdraw_ratio[i] = []
				data_withdraw_ratio[i].push(time);
				data_withdraw_ratio[i].push(parseInt(Number(list[i].total_withdraw)/Number(list[i].total_deposit) * 10000) / 100);
				
				data_total_acc[i] = []
				data_total_acc[i].push(time);
				data_total_acc[i].push(Number(list[i].total_account));
				
				data_active_acc[i] = []
				data_active_acc[i].push(time);
				data_active_acc[i].push(Number(list[i].active_account));
			}

			createChart("chart_invest", "Invest", "Deposit", "Withdraw", data_deposit, data_withdraw, data_withdraw_ratio);
			createChart("chart_acc", "Account", "Total Account", "Active Account", data_total_acc, data_active_acc);			
		});
	}
	
	//$scope.init();
});