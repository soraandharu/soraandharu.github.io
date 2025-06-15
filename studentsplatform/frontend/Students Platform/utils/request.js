// 请求拦截器
const requestInterceptor = (config) => {
  // 添加token认证信息
  const token = uni.getStorageSync('token');
  if (token) {
    config.header = config.header || {};
    config.header.Authorization = 'Bearer ' + token;
  }
  return config;
};

// 响应拦截器
const responseInterceptor = (response) => {
  // 成功情况直接返回数据
  if (response.statusCode >= 200 && response.statusCode < 300) {
    return response.data;
  } 
  // 登录过期处理
  else if (response.statusCode === 401) {
    uni.removeStorageSync('token');
    uni.removeStorageSync('userInfo');
    uni.navigateTo({ url: '/pages/login/index' });
    throw new Error('登录已过期');
  } 
  // 其他错误
  else {
    throw new Error(response.data?.message || '请求失败');
  }
};

// 错误处理函数
const errorHandler = (error) => {
  console.error('请求错误:', error);
  return Promise.reject(error);
};

/**
 * 封装请求函数
 * @param {Object} options - 请求配置
 * @returns {Promise} - 返回请求结果
 */
export function request(options) {
  // 应用请求拦截器
  const config = requestInterceptor(options);
  
  return new Promise((resolve, reject) => {
    uni.request({
      ...config,
      success: (response) => {
        try {
          const result = responseInterceptor(response);
          resolve(result);
        } catch (error) {
          reject(error);
        }
      },
      fail: (error) => {
        errorHandler(error);
        reject(error);
      }
    });
  });
}
