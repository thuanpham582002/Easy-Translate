from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import TwoLineAvatarIconListItem, IconLeftWidget, \
    IconRightWidget

import screens.constant
from model.historytranslate import HistoryTranslate

Builder.load_file('screens/historytranslatescreen.kv')


def get_index_of_item_in_history_translate(item: HistoryTranslate):
    for i in range(len(screens.constant.history_translate)):
        if screens.constant.history_translate[i] is item:
            return i
    return -1


class HistoryTranslateScreen(Screen):
    type = 'history'
    callback = None

    def __init__(self, *args):
        if len(args) == 1:
            self.type = args[0]
        elif len(args) == 2:
            self.type = args[0]
            self.callback = args[1]
        super().__init__()

    def on_pre_enter(self, *args):
        self.ids.history_translate_list.clear_widgets()
        if self.type == 'history':
            for x in reversed(screens.constant.history_translate):
                self.ids.history_translate_list.add_widget(self.get_two_line_avatar_icon_widget(x))
        elif self.type == 'bookmark':
            for x in reversed(screens.constant.history_translate):
                if x.bookmark:
                    self.ids.history_translate_list.add_widget(self.get_two_line_avatar_icon_widget(x))
        return super().on_pre_enter(*args)

    def get_index_of_widget(self, widget):
        if isinstance(widget, IconLeftWidget):
            for i in range(len(self.ids.history_translate_list.children)):
                if widget is self.ids.history_translate_list.children[i].children[1].children[0]:
                    return i
        elif isinstance(widget, IconRightWidget):
            for i in range(len(self.ids.history_translate_list.children)):
                if widget is self.ids.history_translate_list.children[i].children[0].children[0]:
                    return i
        return None

    def trigger_icon_left_release(self, x: IconLeftWidget):
        index_widget = self.get_index_of_widget(x)
        index_item = get_index_of_item_in_history_translate(x.ids['TwoLineAvatarIconListItem'])
        screens.constant.history_translate[index_item].bookmark = not screens.constant.history_translate[
            index_item].bookmark

        for i in range(len(self.ids.history_translate_list.children)):
            if x is self.ids.history_translate_list.children[i].children[1].children[0]:
                index_widget = i
                break

        if self.type == 'history':
            self.ids.history_translate_list.remove_widget(
                self.ids.history_translate_list.children[index_widget])
            self.ids.history_translate_list.add_widget(
                widget=self.get_two_line_avatar_icon_widget(screens.constant.history_translate[index_item]),
                index=index_widget)
        elif self.type == 'bookmark':
            self.ids.history_translate_list.remove_widget(
                self.ids.history_translate_list.children[index_widget])

        screens.constant.save_history_translate()

    def trigger_icon_right_release(self, x: IconRightWidget):
        index_widget = self.get_index_of_widget(x)
        self.ids.history_translate_list.remove_widget(
            self.ids.history_translate_list.children[index_widget])
        # del is used to remove the item from the dictionary
        screens.constant.history_translate.remove(
            screens.constant.history_translate[
                get_index_of_item_in_history_translate(x.ids['TwoLineAvatarIconListItem'])])
        screens.constant.save_history_translate()

    def trigger_item_release(self, x: TwoLineAvatarIconListItem):
        if self.callback is not None:
            self.callback(x.children[1].children[0].ids['TwoLineAvatarIconListItem'])

    def get_two_line_avatar_icon_widget(self, x: HistoryTranslate):
        if x.bookmark:
            print("get_two_line_avatar_icon_star_list_item")
            return self.get_two_line_avatar_icon_star_list_item(x)
        else:
            print("get_two_line_avatar_icon_star_outline_list_item")
            return self.get_two_line_avatar_icon_star_outline_list_item(x)

    def get_two_line_avatar_icon_star_outline_list_item(self, x: HistoryTranslate):
        return TwoLineAvatarIconListItem(IconLeftWidget(
            icon="star-outline",
            on_release=lambda this: self.trigger_icon_left_release(this),
            ids={'TwoLineAvatarIconListItem': x}
        ),
            IconRightWidget(
                icon="delete",
                on_release=lambda this: self.trigger_icon_right_release(this),
                ids={'TwoLineAvatarIconListItem': x}
            ),
            text=x.source_lang + ":" + x.source,
            secondary_text=x.target_lang + ":" + x.target,
            on_release=lambda this: self.trigger_item_release(this))

    def get_two_line_avatar_icon_star_list_item(self, x: HistoryTranslate):
        return TwoLineAvatarIconListItem(IconLeftWidget(
            icon="star",
            on_release=lambda this: self.trigger_icon_left_release(this),
            ids={'TwoLineAvatarIconListItem': x}
        ),
            IconRightWidget(
                icon="delete",
                on_release=lambda this: self.trigger_icon_right_release(this),
                ids={'TwoLineAvatarIconListItem': x}
            ),
            text=x.source_lang + ":" + x.source,
            secondary_text=x.target_lang + ":" + x.target,
            on_release=lambda this: self.trigger_item_release(this)
        )

    def on_leave(self, *args):
        self.ids.history_translate_list.clear_widgets()
        print("on_leave")
        return super().on_leave(*args)
