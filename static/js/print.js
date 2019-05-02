function printJS() {
    var divToPrint = document.getElementById('table');
    var htmlToPrint = ''+
        '<style type="text/css">'+
            '@media print{'+
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
                    'font-size: 3rem;'+
                    'line-height: 110%;'+
                    'margin: 0;'+
                    'float: left !important;'+
                    'text-align: left !important;'+
                '}'+
                'img {'+
                    'max-width: 100%;'+
                    'width: 200px;'+
                    'margin: 0;'+  
                    'margin-top: -10px !important;'+
                '}'+
                '.row {'+
                    'margin-left: auto;'+
                    'margin-right: auto;'+
                    'margin-bottom: 20px;'+
                '}'+
                '.row .col.s8 {'+
                    'width: 66.6666666667%;'+
                    'margin-left: auto;'+
                    'left: auto;'+
                    'right: auto;'+
                '}'+
                '.row .col.s4 {'+
                    'width: 33.3333333333%;'+
                    'margin-left: auto;'+
                    'left: auto;'+
                    'right: auto;'+
                '}'+
                'body{'+
                    "background-image: url('../../static/img/bg-home.png') !important;"+
                    'background-position:left;'+
                    'background-repeat: no-repeat;'+
                    'background-size: cover;'+
                '}'+
            '}'+
        '</style>';
    htmlToPrint += divToPrint.outerHTML;
    newWin = window.open("");
    newWin.document.write(htmlToPrint);
    newWin.print();
    newWin.close();
}