<?php 
	require('routeros_api.class.php');
	
	$API = new RouterosAPI();
	$data = new StdClass();

	if ($API->connect('192.168.20.1','admin','1234')) {

		   $API->write('/interface/print');

		   $READ = $API->read(false);
		   $ARRAY = $API->parseResponse($READ);
		   
		   $API->disconnect();
		   var_dump($ARRAY);

		   $data->estado = 1;
		


	} else {
			$data->estado = 0;
	}
		// echo json_encode($data);
 ?>