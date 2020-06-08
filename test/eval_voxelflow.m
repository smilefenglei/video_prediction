clear; clc;

%subdir and dir_data is the path to save your own results 
%dir_mask is the path of motion_mask
%according to the author, the motion_mask of extraplation is the same as that of interpolation 

subdir = dir('C:/Users/smile/Desktop/DVF_overall/voxel_flow/ucf101_作者share/ucf101_extrap_ours/ucf101_extrap');
dir_data = 'C:/Users/smile/Desktop/DVF_overall/voxel_flow/ucf101_作者share/ucf101_extrap_ours/ucf101_extrap/';
dir_mask = 'C:/Users/smile/Desktop/DVF_overall/voxel_flow/ucf101_作者share/motion_masks_ucf101_interp/motion_masks_ucf101_interp/';

num_img = length(subdir);
flag_valid = zeros(1, num_img, 'single');
mat_psnr = zeros(1, num_img, 'single');
mat_ssim = zeros(1, num_img, 'single');

for id_img = 3:num_img

	dir_img_cur = [dir_data, subdir(id_img).name, '/'];
	dir_mask_cur = [dir_mask, subdir(id_img).name, '/'];

	% read images
	%img_pred = imread([dir_img_cur, 'g_fr.png']);
	%img_target = imread([dir_img_cur, 'frame_02.png']);
	%img_prev = imread([dir_img_cur, 'frame_00.png']);
	%img_next = imread([dir_img_cur, 'frame_01_gt.png']);
	%mask_flow = imread([dir_mask_cur, 'motion_mask.png']);
    
    img_pred = imread([dir_img_cur, 'g_fr.png']);%imread([dir_img_cur, 'frame_02_pred.png']);
	img_target = imread([dir_img_cur, 'frame_02_gt.png']);
	img_prev = imread([dir_img_cur, 'frame_00.png']);
	img_next = imread([dir_img_cur, 'frame_01.png']);
	mask_flow = imread([dir_mask_cur, 'motion_mask.png']);
    

	img_pred_ycbcr = rgb2ycbcr(uint8(img_pred));
	img_target_ycbcr = rgb2ycbcr(uint8(img_target));

	img_pred_gray = img_pred_ycbcr(:, :, 1);
	img_target_gray = img_target_ycbcr(:, :, 1);

	img_pred = single(img_pred);
	img_target = single(img_target);
	img_prev = single(img_prev);

	img_pred_gray = single(img_pred_gray);
	img_target_gray = single(img_target_gray);

	mask_flow = single(mask_flow) ./ 255.0;

	% check validity
	if sum(mask_flow(:)) > 0
		
		flag_valid(id_img) = 1;

		img_pred_mask = repmat(mask_flow, [1, 1, 3]) .* img_pred;
		img_target_mask = repmat(mask_flow, [1, 1, 3]) .* img_target;

		mse = sum((img_pred_mask(:) - img_target_mask(:)).^2) ./ (3 .* sum(mask_flow(:)));
		psnr_cur = 20.0 .* log10(255.0) - 10.0 .* log10(mse);
		
		[ssim_cur, ~] = ssim(rgb2gray(uint8(img_pred_mask)), rgb2gray(uint8(img_target_mask)));

		mat_psnr(id_img) = psnr_cur;
		mat_ssim(id_img) = ssim_cur;

	end

	disp(['Processing Img ', num2str(id_img), '...']);

end

flag_valid(find(mat_psnr == inf)) = 0;
mat_psnr(find(mat_psnr == inf)) = 0;

mean_psnr = sum(flag_valid .* mat_psnr) ./ sum(flag_valid)
mean_ssim = sum(flag_valid .* mat_ssim) ./ sum(flag_valid)
