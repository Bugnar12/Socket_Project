<?php

//function for generating the 3 corresponding arrays
function generateArrays() {
    $n = rand(100, 200);
    $array1 = array_unique(range(1, $n));
    $array2 = array_slice($array1, 0, $n);
    $array3 = array_slice($array1, 0, $n);

    sort($array1);
    shuffle($array2);
    rsort($array3);

    return array($array1, $array2, $array3);
}

//function that preety-prints the required information
function printings(array $array1, array $array2, array $array3){
	$min_best_case = min($array1[0], min($array2[0], $array3[0]));
	$min_average_case = min($array1[1], min($array2[1], $array3[1]));
	$min_worst_case = min($array1[2], min($array2[2], $array3[2]));

	echo "\n";
	echo "The min. no. of steps for Best Case: " . $min_best_case . PHP_EOL;
	echo "The min. no. of steps for Average Case: " . $min_average_case . PHP_EOL;
	echo "The min. no. of steps for the Worst Case: " . $min_worst_case . PHP_EOL;

	echo "------- Bubble Sort -------" . PHP_EOL;
	echo "BC:" . $array1[0] . " , AC:" . $array1[1] . ", WC:" . $array1[2] . PHP_EOL;
	echo "\n";

	echo "------- Merge Sort -------" . PHP_EOL;
	echo "BC:" . $array2[0] . " , AC:" . $array2[1] . ", WC:" . $array2[2] . PHP_EOL;
	echo "\n";

	echo "------- Recursive Selection Sort -------" . PHP_EOL;
	echo "BC:" . $array3[0] . " , AC:" . $array3[1] . ", WC:" . $array3[2] . PHP_EOL;
	echo "\n";
}



$socket = socket_create(AF_INET, SOCK_STREAM, SOL_TCP);
if($socket == false)
{
	echo "Failed to create the socket " . socket_strerror(socket_last_error());
	exit; //return if the creation of the socket could not be done
}

socket_connect($socket, "172.22.227.56", 2345);
$data = generateArrays();
$jsonData = json_encode($data);


socket_send($socket, $jsonData, strlen($jsonData), 0);
echo "Data sent seccessfully! \n";

$response = '';
socket_recv($socket, $response, 100500, 0);
$finalResponse = json_decode($response); //bytes->string

list($result1, $result2, $result3) = $finalResponse;

printings($result1, $result2, $result3);

socket_close($socket); //close the client socket

?>
