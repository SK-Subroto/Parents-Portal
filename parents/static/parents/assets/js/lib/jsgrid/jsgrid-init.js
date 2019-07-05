        $(function() {

            $("#jsGrid").jsGrid({
                height: "100%",
                width: "100%",
                filtering: false,
                editing: true,
                inserting: true,
                sorting: true,
                paging: true,
                autoload: true,
                pageSize: 15,
                pageButtonCount: 5,
                deleteConfirm: "Do you really want to delete the client?",
                controller: db,
                fields: [
                    { name: "Teacher", type: "text", width: 150 },
                    { name: "Date", type: "number", width: 50 },
                    { name: "Work", type: "text",title: "Home Work", width: 200 },
                    { name: "Subject", type: "select", items: db.subjects, valueField: "Id", textField: "Name" },
                    { name: "Check", type: "checkbox", title: "Check", sorting: false },
                    { type: "control" }
                ]
            });

        });