/** @odoo-module **/
import SystrayMenu from 'web.SystrayMenu';
import Widget from 'web.Widget';

var CurrentTimeWidget = Widget.extend({
   template: 'CurrentTimeSystray',

   start: function () {
    var self = this;
    return self._super();
    },
    
});
SystrayMenu.Items.push(CurrentTimeWidget);
export default CurrentTimeWidget;