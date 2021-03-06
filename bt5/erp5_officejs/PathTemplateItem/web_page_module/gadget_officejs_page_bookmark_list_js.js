/*globals window, RSVP, rJS*/
/*jslint indent: 2, nomen: true, maxlen: 80*/
(function (window, RSVP, rJS) {
  "use strict";

  rJS(window)
    .ready(function (g) {
      g.props = {};
      return g.getElement()
        .push(function (element) {
          g.props.element = element;
        });
    })
    .ready(function (g) {
      return new RSVP.Queue()
        .push(function () {
          return RSVP.all([
            g.translate("validated"),
            g.translate("invalidated"),
            g.translate("Not synced!"),
            g.translate("Waiting for approval")
          ]);
        })
        .push(function (result_list) {
          g.props.translation_dict = {
            "validated": result_list[0],
            "invalidated": result_list[1],
            "Not synced!": result_list[2],
            "Waiting for approval": result_list[3]
          };
        });
    })
    .declareAcquiredMethod("translate", "translate")
    .declareAcquiredMethod("getUrlFor", "getUrlFor")
    .declareAcquiredMethod("updateHeader", "updateHeader")
    .declareAcquiredMethod('getSetting', 'getSetting')
    .declareAcquiredMethod("jio_allDocs", "jio_allDocs")
    .allowPublicAcquisition("jio_allDocs", function (param_list) {
      var gadget = this;
      return this.jio_allDocs.apply(this, param_list)
        .push(function (result) {
          var i,
            len;
          for (i = 0, len = result.data.total_rows; i < len; i += 1) {
            // XXX jIO does not create UUID with module inside
            if (result.data.rows[i].id.indexOf("module") === -1) {
              result.data.rows[i].value.state =
                gadget.props.translation_dict["Not synced!"];
            } else {
              result.data.rows[i].value.state =
                gadget.props.translation_dict[
                  result.data.rows[i].value.local_state ||
                    "Waiting for approval"
                ];
            }
          }
          return result;
        });
    })
    .declareMethod("render", function (options) {
      var gadget = this;
      return new RSVP.Queue()
        .push(function () {
          return RSVP.all([
            gadget.getSetting("portal_type"),
            gadget.getSetting("document_title_plural")
          ]);
        })
        .push(function (answer_list) {
          gadget.props.portal_type = answer_list[0];
          gadget.props.bookmark_title_plural = answer_list[1];
          return gadget.getUrlFor({page: "add_bookmark"});
        })
        .push(function (url) {
          return gadget.updateHeader({
            title: gadget.props.bookmark_title_plural,
            add_url: url
          });
        })
        .push(function () {
          return gadget.getDeclaredGadget("listbox");
        })
        .push(function (listbox) {
          return listbox.render({
            search_page: 'bookmark_list',
            search: options.search,
            column_list: [{
              select: 'title',
              title: 'Title'
            }, {
              select: 'url_string',
              title: 'URL'
            }, {
              select: 'description',
              title: 'Description'
            }],
            query: {
              query: 'portal_type:("' + gadget.props.portal_type + '")',
              select_list: ['title', 'url_string', 'description'],
              limit: [0, 30],
              sort_on: [["modification_date", "descending"]]
            }
          });
        });
    });

}(window, RSVP, rJS));