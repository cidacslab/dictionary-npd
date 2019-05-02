function printJS() {
    var divToPrint = document.getElementById('table');
    var htmlToPrint = ''+
        '<style type="text/css">'+
            'table {'+
                'width: 100% !important;'+
                'display: table !important;'+
                'border-collapse: collapse !important;'+
                'border-spacing: 0 !important;'+
            '}'+
            '.print {'+
                'display:block;'+
            '}'+
            '.no-print { '+
                'display:none;'+ 
            '}'+
            'tr {'+
                'border-bottom: 1px solid rgba(0,0,0,0.12);'+
            '}'+
            'td, th {'+
                'padding: 15px 5px;'+
                'display: table-cell;'+
                'text-align: left;'+
                'vertical-align: middle;'+
                'border-radius: 2px;'+
            '}'+
            ' body {'+
                'font: 12pt -apple-system,"BlinkMacSystemFont","Segoe UI","Roboto","Oxygen-Sans","Ubuntu","Cantarell","Helvetica Neue",sans-serif;'+
                'color: #000;'+
            '}'+
            'h1 {'+
                'font-size: 24pt;'+
            '}'+
            'img {'+
                'max-width: 100%;'+
            '}'+
        '</style>';
    htmlToPrint += divToPrint.outerHTML;
    newWin = window.open("");
    newWin.document.write(htmlToPrint);
    newWin.print();
    newWin.close();
}