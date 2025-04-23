import cv2
import base64
from volcenginesdkarkruntime import Ark

def capture_frame_to_base64_with_prefix():
    cap = cv2.VideoCapture(0)  # 0 表示默认摄像头

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return None

    ret, frame = cap.read()
    if ret:
        # 保存帧到本地
        save_path = "captured_frame.jpg"
        cv2.imwrite(save_path, frame)
        print(f"Frame saved to {save_path}")

        # 将帧转换为 JPEG 格式
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()

        # 转换为 base64 编码
        base64_encoded = base64.b64encode(frame_bytes).decode('utf-8')
        prefix = "data:image/jpeg;base64,"
        base64_with_prefix = prefix + base64_encoded
        cap.release()
        return base64_with_prefix
    else:
        print("Error: Could not capture frame.")
        cap.release()
        return None


# 初始化一个Client对象，从环境变量中获取API Key
client = Ark(
    api_key='替换为实际的 API Key',
)

# 从摄像头捕获图片并转换为带前缀的 base64 格式
base64_image = capture_frame_to_base64_with_prefix()


if base64_image:
    response = client.chat.completions.create(
        model="doubao-1-5-thinking-pro-m-250415",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "描述该图片"},
                    {"type": "image_url", "image_url": {"url": base64_image}},
                ],
            }
        ],
    )

    # 提取纯文本内容并自动换行
    print("\n" + response.choices[0].message.content.strip() + "\n")
