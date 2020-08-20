### 1. CUDA설치

본인의 tensorflow version에 맞는 CUDA를 설치해야한다

CUDA설치 사이트 https://developer.nvidia.com/cuda-toolkit-archive

다운로드 후 설치

![참고자료](https://i.stack.imgur.com/VfYKc.png)

### 2. cuDNN설치

cuDNN : CUDA버전과 맞는 VERSION을 다운로드 받고 압축해제 한다(로그인해야됨)

https://developer.nvidia.com/cudnn

---

error 뜰 시 이코드 쓰고 돌리면 됨

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0],enable=True)
os.environ["TF_FORCE_GPU_ALLOW_GROWTH"]="true"