// var config = {
//     "apiKey": "AIzaSyAC4EU24xjMQKXP-41I1TnRDIT4KTN7CV8",
//     "authDomain": "proxy-detection-1df22.firebaseapp.com",
//     "databaseURL": "https://proxy-detection-1df22.firebaseio.com",
//     "projectId": "proxy-detection-1df22",
//     "storageBucket": "proxy-detection-1df22.appspot.com",
//     "messagingSenderId": "17187188207",
//     "appId": "1:17187188207:web:63e8c1f5b50862b1c59a1a",
//     "vmeasurementId": "G-EPTQX1DS4L"
// }
// firebase.initializeApp(config);

var database = firebase.database();





document.getElementById('download').onclick = function download_att() {
    var IClass = document.getElementById('year').value;
    var IDiv = document.getElementById('div').value;
    var csv = 'ATTENDANCE REPORT , DIVISION - \n';
    var data = []
    var subjects = []
    var count = 0;
    document.write("Download Pressed")
    database.ref('/' + IClass + '/' + IDiv).once('value', function(snapshot) {
        snapshot.forEach(function(childSnapshot) {
            // working in Year 
            var stud = []
            var childKey = childSnapshot.key;
            document.write("Working  with roll  ")
            var childData = childSnapshot.val();
            var sub = Object.values(childData)
            var sub_name = Object.keys(childData)

            console.log(sub_name)
            document.write(childKey + "Subject ttendance " + sub + '<br>')
            stud.push(childKey)
            for (index = 0; index < sub.length; index++) {
                if (count == 0) {
                    subjects.unshift("Roll_number")
                    subjects.push(sub_name)
                    count += 1;
                }
                document.write('br>' + sub_name[index] + "-------" + sub[index] + " - - ")
                stud.push(sub[index])
            }
            data.push(stud)
        });

        data.unshift(subjects)
        document.write("Outside Previous Student" + '<br>' + data)
        data.forEach(function(row) {
            csv += row.join(',');
            csv += "\n";
            console.log(subjects);

        });

        document.write('<br><br><br><br>' + "Hello guys" + '<br><br><br><br>')
        var hiddenElement = document.createElement('a');
        hiddenElement.href = 'data:text/csv;charset=utf-8,' + encodeURI(csv);
        hiddenElement.target = '_blank';
        hiddenElement.download = 'Attendance.csv';
        hiddenElement.click();
    });

}