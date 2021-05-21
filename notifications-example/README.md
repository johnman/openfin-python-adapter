# Python Openfin Notification Example

To run this example:

* go to the notification-relay-agent folder
* open a terminal and run npm install
* type: npm run server
* open a second terminal and type: npm run openfin

This will fire up a webserver and run an openfin application that acts
as an agent. The agent will receive a notification object from Python and 
pass it onto the notification api.

The agent also checks the result of a notification interaction. 

If a notification has a button and onClick entry then we check the result of the interaction.

If the result has handler:"agent" then it will check for a url in the result.

If no target is specified then it will launch the url in the system browser.

You have the option of specifying target: "openfin" (open the url in an OpenFin window) or target:"browser" (which will open it in the system browser).

An example of what a notification object will look like can be seen in the example.py file.

More information about Notifications can be found here: https://developers.openfin.co/of-docs/docs/overview-notifications

The default application that is launched shows the window to make it easier to debug. There is a platform config file in the config folder and that application is a platform based application with no UI to show you the different approaches.

*This is an example and not production code. You would not return the notification response back on the message bus this way as you would want to restrict who receives it. You would also restrict who could actually send messages to the agent via the message bus in a real app.* 