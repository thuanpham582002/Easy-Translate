# Easy Translate App for Windows and Android
### made by Pham Tien Thuan, Pham Quoc Viet and Vu Huu Dat for assignment in Python course at PTIT.
- B20DDCCN678 Phạm Tiến Thuận_Leader: Đảm nhiệm phần core, tìm hiểu các thư viện khả thi hay không (ví dụ: thư viện A có hỗ trợ window nhưng lại ko hỗ trợ Android, thư viện A hỗ trợ cả 2 nhưng buildozer không hỗ trợ thư viện A xuất sang APK,...)
    - Tìm hiểu và có demo các logic chức năng của app:
        * Translate text
        * Translate file
        * Translate website
        * Convert and export text từ file.
        * Logic, các thành phần trong api của translate.google.com
        * Text to speech
        * Text copy
    - Tham gia vào các chức năng app:
        * Translate text
        * Translate file
        * Translate website
        * Convert and export text từ file.
        * Text to speech
        * Text copy
        * Clone được giao diện của Google Translate
 
    - Các thư viện đã tìm hiểu và có demo trong ứng dụng:
        * **playsound** - Thư viện phát âm thanh trên window
        * **android.media.MediaPlayer** - Thư viện Java cho phép phát âm thanh
        * **filechooser** - Thư viện mở cửa sổ chọn file trong android và window.
        * **requests** - Dùng để gọi api đến https://translate.google.com/
        * **google-cloud-translate** - Thư viện của google, dùng để dịch tài liệu do không crack được api dịch tài liệu của https://translate.google.com/      
        * **docx**
        * **kivy, kivymd** - thư viện UI multi- platform.
        * **asposecellscloud** - thư viện cho phép convert các xlxs
        * **pynjous** - thư viện cho phép sử dụng các thư viện java trên python.
        * **buildozer** - thư viện cho phép export python sang nhiều platform.
        * **mimetypes** - thư viện cho phép lấy định dạng file.
        
- B20DCCN180 Vũ Hữu Đạt:
    + Tham gia vào quá trình lên ý tưởng thiết kế UI cho app bằng ngôn ngữ kivy
    + Tìm hiểu và triển khai cách thức chuyển đổi file khác nhau sang pdf để phục vụ việc mở file trên nền tảng web dễ dàng hơn
    + Tìm hiểu và triển khai định dạng mở file và đường link trên nền tảng web
    + Thêm tính năng xóa toàn bộ dữ liệu trong bookmark và history
    + Viết chức năng hiển thị thông tin apps
    - Tham gia vào các chức năng app:
            * Translate text
            * Translate file
            * Translate website
            * Convert and export text từ file.
            * Text to speech
                * App UI
            * Chỉnh sửa, tối ưu giao diện trên window
 
    + Các thư viện đã tìm hiểu và demo trong ứng dụng
    
        * **docx2pdf** - Thư viện chuyển đổi file .docx sang .pdf
        * **kivy, kivyMd** - thư viện UI multi - platform
        * **webbrowser** - thư viện cung cấp giao diện cấp cao cho phép hiển thị các tài liệu dựa trên Web cho người dùng.  
        * **google-cloud-translate** - Thư viện của google, dùng để dịch tài liệu do không crack được api dịch tài liệu của https://translate.google.com/
        * **asposecellscloud** - thư viện cho phép convert các xlsx
        * **filechooser** - thư viện cho phép mô tả, chọn file và hiển thị trên window và android
        * **mimetypes** -  thư viện cho phép lấy định dạng file.
        * **base64** - thư viện cung cấp phương thức convert dạng mã hóa 2 chiều từ binary sang string

- B20DCCN731 Phạm Quốc Việt:
    + Cài đặt môi trường ubuntu để làm việc với buidozer.
    + Lên ý tưởng các features của app, phân tích, tổ chức luồng hoạt động của app sao cho đơn giản nhất có thể, hướng tới việc dễ sử dụng đối với người dùng.
    + Test app tại android: text to speech, copy function, UI/UX bugs,...
    + Các thư viện đã tìm hiểu và demo trong ứng dụng
        * **kivy, kivyMd** - thư viện UI multi - platform
        * **webbrowser** - thư viện cung cấp giao diện cấp cao cho phép hiển thị các tài liệu dựa trên Web cho người dùng.
        * **asposecellscloud** - thư viện cho phép convert các xlsx
 
        * **filechooser** - thư viện cho phép mô tả, chọn file và hiển thị trên window và android
        * **android.media.MediaPlayer** - thư viện Java cho phép phát âm thanh
        * **buildozer** - thư viện cho phép export python sang nhiều platform.
        * **pynjous** - thư viện cho phép sử dụng các thư viện java trên python.
 
 
    + Module đảm nhiệm:
        * Thiết lập giao diện người dùng tối ưu cho sự đơn giản dễ dùng bằng kivy phù hợp trên android.
        * Text to speech với đa ngôn ngữ , function copy.
        Tìm hiểu về pynjous và triển khai để import các framework của android vào python.
        * Triển khai MediaPlayer của android để phát Audio tại các thiết bị android. ( thay đổi pitch, accent giọng của AI nói từ text)
        Sử dụng bulldozer để export sang app ở dạng apk để cài đặt vào các thiết bị android.
        * Debug, test apk trên emulator của android studio ( android R trở lên) và máy thật ( dưới android R)
        * Thiết lập tính năng đa ngôn ngữ cho app ( tiếng anh / tiếng việt)
    + Clean code ( dọn dẹp những phần không cần thiết trong code)
    
## Description
- This is a simple app that allows you to translate text from one language to another.
- Easy Translate is available for both Windows and Android.
- This app is still in beta, so there might be some potential bugs.
- Easy Translate is written in Python using Kivy library for interactive user interface.
## Features
- Translate text from one language to another.
- Translate text from text.
- Translate text from image. (coming soon)
- Translate text from voice. (coming soon)
- Translate text from file (txt, docx, pdf, etc). 
- Translate text from url (web page).
- Convert document to html.
- Local history and bookmark
## How to use
- Download the app for your device.
- Open the app.
- Select the language you want to translate from.
- Select the language you want to translate to.
- Type the text you want to translate.
- Click the translate button.
- The translated text will appear.
## Download
- [Windows]( Coming Soon )
- [Android]( Coming Soon )
## Screenshots
### Windows
<table>
    <tr>
        <td><strong>Homescreen</strong></td>
        <td><strong>Select language</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/window/windows_home.png" width="100%"></td>
        <td><img src="screenshots/window/windows_search_language.png" width="100%"></td>
    <tr>
        <td><strong>File Chooser</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/window/windows_file_translate.png" width="100%"></td>
    <tr>
        <td><strong>Bookmark</strong></td>
        <td><strong>History</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/window/windows_bookmark.png" width="100%"></td>
        <td><img src="screenshots/window/windows_history.png" width="100%"></td>
    </tr>
    <tr>
        <td><strong>Screen Translate Text</strong></td>
        <td><strong>Detect Url Translate Web</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/window/windows_screen_translate_text.png" width="100%"></td>
         <td><img src="screenshots/window/windows_detect_url_translate.png" width="100%"></td>
    </tr>
</table>

### Android
<table>
    <tr>
        <td><strong>Homescreen</strong></td>
        <td><strong>Select language</strong></td>
        <td><strong>File Chooser</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/android/android_home.png" width="100%"></td>
        <td><img src="screenshots/android/android_search_language.png" width="100%"></td>
        <td><img src="screenshots/android/android_file_translate.png"></td>
    <tr>
        <td><strong>Bookmark</strong></td>
        <td><strong>History</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/android/android_bookmark.png" width="100%"></td>
        <td><img src="screenshots/android/android_history.png" width="100%"></td>
    </tr>
    <tr>
        <td><strong>Screen Translate Text</strong></td>
        <td><strong>Detect Url Translate Web</strong></td>
    </tr>
    <tr>
        <td><img src="screenshots/android/android_screen_translate_text.png" width="100%"></td>
         <td><img src="screenshots/android/android_detect_url_translate.png" width="100%"></td>
    </tr>
</table>

## Credits
- [Python](https://www.python.org/)
- [Kivy](https://kivy.org/)
- [Google Translate](https://translate.google.com/)
- [Google Translate API](https://pypi.org/project/googletrans/)
